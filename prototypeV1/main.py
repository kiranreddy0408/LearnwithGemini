from flask import Flask, render_template
from flask import Flask, request, jsonify, session, redirect
import logging
import google.generativeai as genai
from dotenv import load_dotenv
import os
import sys
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.secret_key = 'eduelite'
app.logger.setLevel(logging.INFO)  # Set log level to INFO
handler = logging.FileHandler('app.log')  # Log to a file
app.logger.addHandler(handler)

def gemini_call(input_text):
    try:
        
        app.logger.info('This is an INFO message')
        load_dotenv()
        os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(input_text)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")

def generate_mock_interview(company,topics,difficulty,no_of_questions,interview_description):
    input_text = f'Generate {no_of_questions} interview questions for a {difficulty.lower()} difficulty mock interview at {company} on the following topics: {topics}. The interview description is: "{interview_description}" in the format: {{"questions":["q1","q2"]}}'
    response=gemini_call(input_text)
    original_string = response.text
    json_string = str(original_string)
    clean_json_string = json_string.replace("\n", "").replace("**", "").replace("\'","")
    parsed_json = json.dumps(clean_json_string)
    return clean_json_string

def generate_mock_analysis(data, question):
    input_text = f'Analyze the provided mock interview response {data} for the given question {question}. Evaluate alignment, grammar, tone, and suggest improvements. Be very strict in the analysis. If the provided response does not match the given question, provide negative feedback. Provide analysis in this format: {{"correctness":["Alignment evaluation analysis","how close is the answer"],"grammar":["Spelling and errors analysis","Grammar analysis"],"tone":["Tone assessment formal or informal analysis","Overall tone analysis"],"improvements":["Suggestions based on response","some more Suggestions"],"correct_ans":["correct answer","a direct link-resource URL for correct answer"]}}'
    
    while True:
        response = gemini_call(input_text)  # Assuming gemini_call is the function that makes the API call
        
        original_string = response.text
        json_string = str(original_string)
        clean_json_string = json_string.replace("\n", "").replace("**", "").replace("\'","")
        parsed_json = json.dumps(clean_json_string)
        
        if clean_json_string.startswith('{'):
            print(clean_json_string)
            return clean_json_string  # Return the clean JSON string if it starts with '{'
        else:
            # If the response does not start with '{', continue the loop and make another call
            continue


def generate_quiz_pl(data):
    board = data.get('board')
    selected_class = data.get('class')
    selected_subject = data.get('subject')
    selected_chapter = data.get('chapter')
    # Construct input text based on passed arguments
    # input_text = f'Generate {num_questions} quiz questions of difficulty level <{difficulty}> on {quiz_topic} with explanation in 2 lines in the following format strictly avoid other text  {{"q":{{"q1":{{"question":"question","op":["opt1","opt2","opt3","opt4"],"a":0,"e":"explanation"}}}}}}'
    input_text = f'Generate 5 quiz questions on the subject "{selected_subject}" of chapter "{selected_chapter}" for class {selected_class} under the {board} board. Provide explanations along with options and indicate the correct answer in the format: {{"q":{{"q1":{{"question":"Question here","opt":["Option 1","Option 2","Option 3","Option 4"],"ans":0,"exp":"Explanation here"}}}}}}'
    response=gemini_call(input_text)
    original_string = response.text
    json_string = str(original_string)
    clean_json_string = json_string.replace("\n", "").replace("**", "").replace("\'","")
    parsed_json = json.dumps(clean_json_string)
    return clean_json_string

def generate_quiz(data):
    board = data.get('board')
    selected_class = data.get('class')
    selected_subject = data.get('subject')
    selected_chapter = data.get('chapter')
    no_of_q=data.get('num_of_questions')
    difficulity=data.get('difficulity')
    # Construct input text based on passed arguments
    # input_text = f'Generate {num_questions} quiz questions of difficulty level <{difficulty}> on {quiz_topic} with explanation in 2 lines in the following format strictly avoid other text  {{"q":{{"q1":{{"question":"question","op":["opt1","opt2","opt3","opt4"],"a":0,"e":"explanation"}}}}}}'
    input_text = f'Generate { no_of_q} of {difficulity} quiz questions on the subject "{selected_subject}" of chapter "{selected_chapter}" for class {selected_class} under the {board} board. Provide explanations along with options and indicate the correct answer in the format: {{"q":{{"q1":{{"question":"Question here","opt":["Option 1","Option 2","Option 3","Option 4"],"ans":0,"exp":"Explanation here"}}}}}}'
    response=gemini_call(input_text)
    original_string = response.text
    json_string = str(original_string)
    clean_json_string = json_string.replace("\n", "").replace("**", "").replace("\'","")
    parsed_json = json.dumps(clean_json_string)
    return clean_json_string

def generate_quiz_report(data):
    # board = data.get('board')
    # selected_class = data.get('class')
    # selected_subject = data.get('subject')
    # selected_chapter = data.get('chapter')
    # Construct input text based on passed arguments
    # input_text = f'Generate {num_questions} quiz questions of difficulty level <{difficulty}> on {quiz_topic} with explanation in 2 lines in the following format strictly avoid other text  {{"q":{{"q1":{{"question":"question","op":["opt1","opt2","opt3","opt4"],"a":0,"e":"explanation"}}}}}}'
    input_text = f'Analyze this quiz test response {data} and provide weak topics based on analysis. Additionally, list one or two prerequisite topics that should be known to understand the present topic. Format the response as follows: {{"weakTopics": ["topic1", "topic2"], "prerequisiteTopics": ["topic1", "topic2"]}}'
    response=gemini_call(input_text)
    original_string = response.text
    json_string = str(original_string)
    clean_json_string = json_string.replace("\n", "").replace("**", "").replace("\'","")
    parsed_json = json.dumps(clean_json_string)
    print(clean_json_string)
    return clean_json_string

def generate_sub_modules(topic_name):
    input_text = f'Generate 4-5 submodules for this topic {topic_name}  in this format: {{"sub_modules":["sub-module1","sub-module2"]}}'
    response=gemini_call(input_text)
    original_string = response.text
    json_string = str(original_string)
    clean_json_string = json_string.replace("\n", "").replace("**", "").replace("*", "").replace("\'","")
    parsed_json = json.dumps(clean_json_string)
    print(clean_json_string)
    return clean_json_string

def generate_sub_modules_content(submodule_name,topic_name):
    input_text = f'Provide in detail explanation for this topic {submodule_name} of this main topic {topic_name} with resources urls strictly in this format(""dont include any title or extra other than this format""):{{"explaination":["explanation content without any links"],"resources":["direct-link1","direct-link2"],"videolinks":["https://www.youtube.com/results?search_query={topic_name}","https://www.youtube.com/results?search_query={topic_name}"]}}'
    while True:
        response = gemini_call(input_text)  # Assuming gemini_call is the function that makes the API call
        
        original_string = response.text
        json_string = str(original_string)
        clean_json_string = json_string.replace("\n", "").replace("**", "").replace("\'","")
        parsed_json = json.dumps(clean_json_string)
        
        if clean_json_string.startswith('{'):
            print(clean_json_string)
            return clean_json_string  # Return the clean JSON string if it starts with '{'
        else:
            # If the response does not start with '{', continue the loop and make another call
            continue
    
    # Returning the extracted data as JSON
    return json.dumps({'explanation': explanation, 'resources': resources, 'videolinks': videolinks})


     
   

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index.html')
def indexhtml():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/about.html')
def about():
    return render_template('about.html')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')
@app.route('/service')
def service():
    return render_template('service.html')
@app.route('/personalized-learning')
def personalize_learning():
    return render_template('personalized-learning.html')

@app.route('/psl')
def pslearning():
    return render_template('personalizedlearn.html')
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/testpage', methods=['POST'])
def render_testpage():
    # Retrieve the data from the form
    quiz_data = request.form.get('quiz_data')

    # Pass the data to the testpage.html template
    return render_template('testpage.html', quiz_data=quiz_data)

@app.route('/validate', methods=['POST'])
def validate_quiz():
    submission_data = request.json
    
    
    print(submission_data)
    report=generate_quiz_report(submission_data)
    return report

@app.route('/testreport', methods=['POST'])
def test_report():
    report = request.form.get('report')
    print(report)

    # Pass the data to the testpage.html template
    return render_template('testreport.html', report=report)

@app.route('/loginuser', methods=['POST'])
def loginuser():
    print(request.form)
    login_as = request.form.get('login_as')
    user_type = request.form.get('user_type')
    print(login_as)
    print(user_type)
    # username = request.form['username']
    # password = request.form['password']
    
    # Assuming you have some validation logic here
    
    # Store data in session
    session['login_as'] = login_as
    session['user_type'] = user_type
        # session['username'] = username
    if (login_as == "teacher" or login_as == "parent"):
        return redirect('/dashboard')
    else:
        return redirect('/')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        login_as = session['login_as']
        user_type = session['user_type']
        username = session['username']
        
        # You can render the dashboard template and pass these session variables
    if( session['user_type']=="high-school"):
        return render_template('ugdashboard.html')
    else:
        return  render_template('studentdashboard.html') # Redirect to login page if user is not logged in


@app.route('/learn')
def learn_topic():
    # Extract the topic name from the query parameter
    topic_name = request.args.get('topic')
    sub_modules=generate_sub_modules(topic_name)

    # Render the learn page with the topic name
    return render_template('learn.html', topic_name=topic_name,sub_modules=sub_modules)


# Example route that handles submodule information
@app.route('/get_module_content', methods=['POST'])
def get_module_content():
    data = request.json
    submodule_name = data['submodule']
    topic_name = data['topic_name']
    print(submodule_name)
    # Process the submodule_name to get relevant content
    # For demonstration, returning a simple response
    response_content = generate_sub_modules_content(submodule_name,topic_name)
    return jsonify({'content': response_content})




@app.route('/test', methods=['POST'])
def test_route():
    # Retrieve data from the request
    data = request.json

    # Process the data
    board = data.get('board')
    selected_class = data.get('class')
    selected_subject = data.get('subject')
    selected_chapter = data.get('chapter')

    # Example: Print the retrieved data
    print("Board:", board)
    print("Class:", selected_class)
    print("Subject:", selected_subject)
    print("Chapter:", selected_chapter)

    # You can perform further processing here, like database operations, etc.

    # Prepare a response if needed
    # response_data = {
    #     'message': 'Data received successfully',
    #     'data': data
    # }

    # Return a response (JSON)
    return generate_quiz_pl(data)

@app.route('/quizgene', methods=['POST'])
def quiz_route():
    # Retrieve data from the request
    data = request.json

    
    return generate_quiz(data)

@app.route('/mockint')
def mockinterview():
    return render_template('mock-interview.html')

@app.route('/mockintpage', methods=['POST'])
def mockinterviewgen():
    if request.method == 'POST':
        # Retrieve form data
        company = request.form['company']
        topics = request.form['topics']
        difficulty = request.form['difficulty']
        no_of_questions = request.form['no_of_questions']
        interview_description = request.form['interview_description']
        intdata=generate_mock_interview(company,topics,difficulty,no_of_questions,interview_description)
        print(intdata)
        return render_template('mockint-rec.html',intdata=intdata,topics=topics)
    
@app.route('/mockanalysis', methods=['POST'])
def mockinterviewanalysis():
    if request.method == 'POST':
        data = request.json
        answer = data['answer']
        question = data['question']
        print(answer)
        # Now you can use answer and question in your function
        analysis=generate_mock_analysis(answer, question)
        return jsonify({'content':analysis })











if __name__ == '__main__':
    app.run(debug=True)
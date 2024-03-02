from flask import Flask, render_template
from flask import Flask, request, jsonify, session, redirect
import logging
import google.generativeai as genai
import sys
import json
app = Flask(__name__)
app.secret_key = 'eduelite'
app.logger.setLevel(logging.INFO)  # Set log level to INFO
handler = logging.FileHandler('app.log')  # Log to a file
app.logger.addHandler(handler)

def gemini_call(input_text):
    try:
        
        app.logger.info('This is an INFO message')
        genai.configure(api_key='AIzaSyDJ9CpL8Ms070AAzWXGB1Aes3TA2zKM0OM')
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(input_text)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")


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
    clean_json_string = json_string.replace("\n", "").replace("**", "").replace("\'","")
    parsed_json = json.dumps(clean_json_string)
    print(clean_json_string)
    return clean_json_string

def generate_sub_modules_content(topic_name):
    input_text = f'Generate in detail explanation for this topic {topic_name} with resources urls in this format:{"content"}'
    response=gemini_call(input_text)
    original_string = response.text
    json_string = str(original_string)
    clean_json_string = json_string.replace("\n", "").replace("**", "").replace("\'","")
    parsed_json = json.dumps(clean_json_string)
    return original_string
     
   

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
    print(submodule_name)
    # Process the submodule_name to get relevant content
    # For demonstration, returning a simple response
    response_content = generate_sub_modules_content(submodule_name)
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











if __name__ == '__main__':
    app.run(debug=True)
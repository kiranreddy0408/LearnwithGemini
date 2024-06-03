import logging
import google.generativeai as genai
from dotenv import load_dotenv
import os
import sys
import json
def gemini_call(input_text):
    try:
        
  
        load_dotenv()
        os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(input_text)
        # for image in response.images:
        #     print(image, "\n\n----------------------------------\n")
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")

gemini_call("explain this topic 'hybridization of sp2 orbitals' with an explanation and online resources and a example image link if any possible. give all content in this json object format:{'explanation':explanation,'resource-links':['link1','link2'],'image-link':link}")
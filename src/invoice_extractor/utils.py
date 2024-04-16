# Importing dependencies and loading environment variables

import google.generativeai as genai
import os
from dotenv import load_dotenv
from src.invoice_extractor.logger import logging

load_dotenv()
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

# Now, let us create a function to load the image and extract the text from it using Gemini Pro Vision Model

def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    
    return response.text


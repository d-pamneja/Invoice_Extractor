# Importing dependencies and loading environment variables

import google.generativeai as genai
import os
from dotenv import load_dotenv
from src.invoice_extractor.logger import logging

load_dotenv()
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

# Now, let us create a function to load the image and extract the text from it using Gemini Pro Vision Model

def get_gemini_response(input,image,prompt): 
    # Here, we load the model and generate a response based on the given parameters of input, image and prompt as a list
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    
    return response.text


def input_image_setup(file):
    # Here, we convert the image data into bytes and setup the image as a list of json object with the requried data to read the image
    try:
        if file is not None:
            bytes_data = file.getvalue() # Converts the image into bytes
            
            image = [
                {
                    "mime_type" : file.type,
                    "data" : bytes_data
                }
            ]
            
            return image
    except:
        raise FileNotFoundError("No file has been uploaded.")
    



    

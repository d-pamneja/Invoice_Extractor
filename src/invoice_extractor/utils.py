# Importing dependencies and loading environment variables
import base64
import google.generativeai as genai
import openai
import os
from dotenv import load_dotenv
from src.invoice_extractor.logger import logging

load_dotenv()
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))
openai.api_key = os.getenv('OPENAI_API_KEY')


# Now, let us create a function to load the image and extract the text from it using Gemini Pro Vision Model


# def encode_image(image_path): # GEMINI CODE - DO NOT ALTER
#   with open(image_path, "rb") as image_file:
#     return base64.b64encode(image_file.read()).decode('utf-8')

# def get_gemini_response(input,image,prompt): # GEMINI CODE - DO NOT ALTER
#     # Here, we load the model and generate a response based on the given parameters of input, image and prompt as a list
#     model = genai.GenerativeModel('gemini-pro-vision')
#     response = model.generate_content([input,image[0],prompt])
    
#     return response.text



def get_chatgpt_response(input_text, image, prompt):        
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": input_text},
        {"role": "user", "content": [
            prompt,
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image}"
                }
            }
            ]
        }
    ]

    
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )

    logging.info(response.choices[0].message.content)
    return response.choices[0].message.content


# def input_image_setup(file): # GEMINI CODE - DO NOT ALTER
#     # Here, we convert the image data into bytes and setup the image as a list of json object with the requried data to read the image
#     try:
#         if file is not None:
#             bytes_data = file.getvalue() # Converts the image into bytes
            
#             image = [
#                 {
#                     "mime_type" : file.type,
#                     "data" : bytes_data
#                 }
#             ]
            
#             return image
#         # return bytes_data
#     except:
#         raise FileNotFoundError("No file has been uploaded.")
    
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# def input_image_setup(file): # GEMINI CODE - DO NOT ALTER
#     # Here, we convert the image data into bytes
#     try:
#         if file is not None:
#             bytes_data = file.read()  # Read the file directly
#             print(bytes_data)
#             print("\n\n\n\n----------------------\n\n\n\n")
#             return bytes_data
#         else:
#             raise FileNotFoundError("No file has been uploaded.")
#     except Exception as e:
#         raise FileNotFoundError(f"Error in loading the file: {str(e)}")



    

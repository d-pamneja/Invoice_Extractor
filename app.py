# Importing the dependencies and loading environment variables

from dotenv import load_dotenv
import os
import base64
import streamlit as st
from PIL import Image
import google.generativeai as genai
from src.invoice_extractor.logger import logging
from src.invoice_extractor.utils import get_chatgpt_response,encode_image
from src.invoice_extractor.prompts import review_input,prompt_review,prompt_specific

load_dotenv()
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

# Initialising the Streamlit Application

st.set_page_config(page_title="Invoice Extractor using Gemini Vision")

st.header("Gemini Application")

type_prompt_list = ["Specific","Review"]
type_prompt = st.selectbox("Type of Query",type_prompt_list)

if type_prompt != "Review":
    input = st.text_input("Enter the Input Prompt",key="input")

    
uploaded_file = st.file_uploader("Chosse the invoice..",type=["jpg","jpeg","png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_path = os.path.join("./uploads",uploaded_file.name)
    image.save(image_path)
    st.image(image,caption="Uploaded Image",use_column_width=True)
    

    
submit = st.button("Submit")

if submit:
    logging.info("----------------------------START------------------------------")
    base64_image = encode_image(image_path)
    if type_prompt != "Review":
        # response = get_gemini_response(input,image_data,prompt_specific) # GEMINI CODE - DO NOT ALTER
        response = get_chatgpt_response(input,base64_image,prompt_specific)
        logging.info("Specific Question Response Loaded")
    else:
        # response = get_gemini_response(review_input,image_data,prompt_review) # GEMINI CODE - DO NOT ALTER
        response = get_chatgpt_response(review_input,base64_image,prompt_review)
        logging.info("Review Response Loaded.")


    st.subheader("The answer is as follows : ")
    st.write(response)
    logging.info("----------------------------END------------------------------")
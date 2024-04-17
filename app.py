# Importing the dependencies and loading environment variables

from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai
from src.invoice_extractor.logger import logging
from src.invoice_extractor.utils import input_image_setup, get_gemini_response
from src.invoice_extractor.prompts import review_input,prompt_review,prompt_specific

load_dotenv()
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

# Initialising the Streamlit Application

st.set_page_config(page_title="Invoice Extractor using Gemini Vision")

st.header("Gemini Application")

type_prompt_list = ["Specific","Review"]
type_prompt = st.selectbox("Type of Query",type_prompt_list)

if type_prompt is not "Review":
    input = st.text_input("Enter the Input Prompt",key="input")

    
uploaded_file = st.file_uploader("Chosse the invoice..",type=["jpg","jpeg","png"])
image = ""

if uploaded_file is not None:
    # Once the upload is done, display the image once to the user
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)
    

    
submit = st.button("Submit")

if submit:
    image_data = input_image_setup(uploaded_file)
    if type_prompt is not "Review":
        response = get_gemini_response(input,image_data,prompt_specific)
    else:
        response = get_gemini_response(review_input,image_data,prompt_review)


    st.subheader("The answer is as follows : ")
    st.write(response)
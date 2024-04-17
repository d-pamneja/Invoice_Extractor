# Importing the dependencies and loading environment variables

from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai
from src.invoice_extractor.logger import logging

load_dotenv()
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

# Initialising the Streamlit Application

st.set_page_config(page_title="Invoice Extractor using Gemini Vision")

st.header("Gemini Application")
input = st.text_input("Enter the Input Prompt",key="input")
uploaded_file = st.file_uploader("Chosse the invoice..",type=["jpg","jpeg","png"])
image = ""

if uploaded_file is not None:
    # Once the upload is done, display the image once to the user
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)
    
submit = st.button("Review the Invoice")


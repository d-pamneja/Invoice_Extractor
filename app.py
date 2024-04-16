# Importing the dependencies and loading environment variables

from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai
from src.invoice_extractor.logger import logging

load_dotenv()
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

logging.info("App Running")
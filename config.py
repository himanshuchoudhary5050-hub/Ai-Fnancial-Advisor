import streamlit as st
from google import genai

# Load API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Create Gemini client
client = genai.Client(api_key=api_key)

# Use a stable model
MODEL_NAME = "gemini-2.0-flash"

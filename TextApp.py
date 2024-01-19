from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")


def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


st.header("Gemini LLM Application")

input = st.chat_input("Input Prompt")
submit = st.button("Ask")

if submit:
    response = get_gemini_response(input)
    st.write(response)

from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")


def get_gemini_response(image, input=""):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text


st.header("Gemini LLM Application")

input = st.chat_input("Input Prompt")

upload=st.file_uploader('Choose an image',type=['jpg','jpeg','png'])

if upload is not None:
    image=Image.open(upload)
    st.image(image,caption='Uploaded Image',use_column_width=True)

submit=st.button('Tell me about button')

if submit:
    response=get_gemini_response(image,input)
    st.header('Response')
    st.write(response)
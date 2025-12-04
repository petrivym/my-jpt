import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("GPT Web Service")

prompt = st.text_area("Enter your prompt:")

if st.button("Submit"):
    if prompt:
        with st.spinner("thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                answer = response.choices[0].message.content
                st.success(answer)
            except Exception as e:
                st.error(f"Error: {e}")
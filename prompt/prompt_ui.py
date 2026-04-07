from pathlib import Path

from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

st.header("LangChain Prompt UI")

user_input = st.text_input("Enter your name:")

prompt_path = Path(__file__).with_name("nobel_prize_prompt.json")
template = load_prompt(str(prompt_path))

prompt = template.invoke({
    "name": user_input
})

if st.button("Submit"):
    response = model.invoke(prompt)
    st.write("Response:")
    st.write(response.content) 
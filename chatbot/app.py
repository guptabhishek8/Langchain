from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
# if using openAI API
# from langchain_openai import ChatOpenAI 

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# env variable
# os.environ["OPEN_API_KEY"] = os.getenv("OPENAI_API_KEY")


# Lamgsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true" 
os.environ["LANGCHAIN_PROJECT"] =  os.getenv("LANGCHAIN_PROJECT")


## creating chatbot
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant, Please provide response to the user queries"),
        ("user", "Question: {question}")
    ]
) 

# streamlit framework
st.title("Langchain Demo with Llama2 API")
input_text = st.text_input("Search the Topic you want")

# OLLAMA LLM Call
# llm = chatOpenAI(model = "gpt-3.5-turbo")
llm  = OllamaLLM(model = "llama2")
output_parser = StrOutputParser()

# chain
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))



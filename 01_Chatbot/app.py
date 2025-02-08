from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv() 

# Azure OpenAI API Keys
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")
os.environ["OPENAI_DEPLOYMENT_NAME"] = os.getenv("OPENAI_DEPLOYMENT_NAME")
os.environ["OPENAI_API_VERSION"] = os.getenv("OPENAI_API_VERSION")

# Langsmith Tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])

# Streamlit UI
st.title('Chatbot using Langchain')
input_text = st.text_input('Search the topic you want')

# Azure OpenAI LLM
llm = ChatOpenAI(
    azure_deployment=os.getenv("OPENAI_DEPLOYMENT_NAME"),  
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_version=os.getenv("OPENAI_API_VERSION")
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({'question': input_text})
    st.write(response)

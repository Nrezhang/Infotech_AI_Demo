import openai
import json
import requests
from dotenv import load_dotenv
import os
from langchain.chains.llm import LLMChain
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain, SQLDatabaseSequentialChain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.chat_models import ChatOpenAI

from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.prompts import PromptTemplate
import streamlit as st

from customprompt import PROMPT


class LLMhelper:
    def __init__(self, deployment_name: str = None, llm: OpenAI = None, prompt: str = "", temperature: float = None, max_tokens: int = -1):
        load_dotenv()
        deployment_name = "gpt-4-1106-preview" 
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", 0.7)) if temperature is None else temperature
        self.prompt = PROMPT if prompt == "" else prompt
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", -1)) if max_tokens == -1 else max_tokens
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.llm: ChatOpenAI = ChatOpenAI(model_name=deployment_name, engine=deployment_name, temperature=self.temperature, max_tokens=self.max_tokens if self.max_tokens != -1 else None) if llm is None else llm



    #initial test to see if the api is working
    def chat(x: str):
        response = openai.chat.completions.create(
                    model = self.deployment_name,   # resouce not found
                    messages=[
                        {"role": "system", "content": "You are a web developer"},
                        {"role": "user", "content": x},
                    ]
                )
        # print the response
        return response.choices[0].message.content


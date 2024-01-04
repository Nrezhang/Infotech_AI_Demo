import os
from dotenv import load_dotenv

import openai
import psycopg2
from langchain.llms.openai import OpenAI

from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.sql_database import SQLDatabase

load_dotenv()

class LLMHelper:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
    
    def checkdb(question):

        llm=OpenAI(openai_api_key= os.getenv("OPENAI_API_KEY"), deployment_name=os.getenv("OPENAI_DEPLOYMENT_NAME"), temperature = 0.2)

        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="dev",
            password="")
        db = SQLDatabase.from_uri(
             "postgresql+psycopg2://dev:@localhost:5432/postgres",
            )
        toolkit = SQLDatabaseToolkit(db=db, llm=llm)

        agent_executor = create_sql_agent(
            llm=OpenAI(temperature=0),
            toolkit=toolkit,
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        )

        result = agent_executor.run(question)
        return result
    
    def cut_string_before_double_slash(input_string):
        index_of_double_slash = input_string.find("//")
        
        if index_of_double_slash != -1:
            result_string = input_string[index_of_double_slash + 2:]
            return result_string
        else:
            return input_string

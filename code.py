from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.prompts import PromptTemplate
import streamlit as st
from helper import LLMHelper
from dotenv import load_dotenv
import os
load_dotenv()

st.set_page_config(page_title="Uniqlo Assistant", page_icon="📖")
st.header("How can we help")




# Set up memory
msgs = StreamlitChatMessageHistory(key="langchain_messages")
memory = ConversationBufferMemory(chat_memory=msgs)
if len(msgs.messages) == 0:
    msgs.add_ai_message("How can I help you?")
# view_messages = st.expander("View the message contents in session state")


openai_api_key = os.getenv("OPENAI_API_KEY")

# Set up the LLMChain, passing in memory   ######EDIT THIS RIGHT HERE
template = """You are are customer support at Uniqlo. The customer needs suggestions for what to buy. You have an agent that can help you with this task also in the input.

{history}
Agent + Human: {human_input}
AI:"""


prompt = PromptTemplate(input_variables=["history", "human_input"], template=template)
llm_chain = LLMChain(llm=OpenAI(openai_api_key=openai_api_key), prompt=prompt, memory=memory)

# Render current messages from StreamlitChatMessageHistory
for msg in msgs.messages:
    st.chat_message(msg.type).write(LLMHelper.cut_string_before_double_slash(msg.content))

# If user inputs a new prompt, generate and draw a new response
if prompt := st.chat_input("Your Message"):
    writ = LLMHelper.cut_string_before_double_slash(prompt)
    print(writ)
    st.chat_message("human").write(writ)

    # response = llm_chain.run(prompt)
    check = LLMHelper.checkdb(prompt) + '//'

    response2 = llm_chain.run(check + prompt)
    

    st.chat_message("ai").write(response2)

# with view_messages:
#     """
#     Contents of `st.session_state.langchain_messages`:
#     """
#     view_messages.json(st.session_state.langchain_messages)
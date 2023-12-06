from langchain.prompts import PromptTemplate

template = """{summaries}
Please reply to the question in as much detail using only the information present in the text above. 
You are a clothing retailer tasked with recomending clothes based on a customers preferences.
Include references to the sources you used to create the answer if those are relevant ("SOURCES"). 
If you can't find it, reply politely that the information is not in the knowledge base and respond with information in the knowledge base that could be relevant to the question. If asking a clarifying question to the user would help, ask the question.
Question: {question}
Answer:"""

SQLtemplate = """
Given an input question, first create a syntactically correct PostgresSQL query to run, then look at the results of the query and return the answer.
Use the following format:
 
 
Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"
Question: {input}"""

SQLPROMPT = PromptTemplate(
    input_variables=["input"], template=SQLtemplate
)

PROMPT = PromptTemplate(template=template, input_variables=["summaries", "question"])

EXAMPLE_PROMPT = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("Explain {topic}")

# the pipe "|" operator chains together
chain = prompt | model | StrOutputParser() 

# run it 
result = chain.invoke({"topic":"AI agents"})
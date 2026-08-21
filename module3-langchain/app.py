# Prompt Template — Steering the Model
# Prompts are reusable templates with placeholders- They let you build dynamic instructions for the LLM.

from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variable = ["topic"],
    template = "Explain {topic} to a beginner"
)

#fill the placeholder
prompt = template.format(topic = "LangChain")

# Result:
# "Explain LangChain to a beginner"
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()

model = init_chat_model("openai:gpt-4o")


@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b


@tool
def divide(a: float, b: float) -> float:
    """Divide the first number by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


agent = create_agent(
    model=model,
    tools=[multiply, divide],
)

result = agent.invoke({
    "messages": [
        ("user", "What is 15 multiplied by 8, then divided by 3?")
    ]
})

print(result["messages"][-1].content)

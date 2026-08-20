
# ------------------------
# STEP 1: Initialize Model
# ------------------------

from langchain.chat_models import init_chat_model
model = init_chat_model("openai:gpt-4o-mini")


# ------------------------
# STEP 2: Define Tools
# ------------------------
# Each tool needs: a name, a clear docstring, and type hints. LLM reads these to decide when and how to use each tool


# Decorators (@tool)
# @tool wraps a function so the agent
# framework can register it as a callable tool.
# Think of @ as a label you stick on a function
# to give it special powers - the function itself
# doesn't change.

# @tool Decorator — registers this function as a tool the agent can discover and call

# a: float Type hints — tells the LLM what data types to pass (auto-generates JSON schema)

# -> float Return type — tells the agent what kind of data the tool sends back

# """ """ Docstring — the LLM reads this to decide when to use this tool.
# Clear description = accurate tool selection

# What the LLM sees: The framework converts your decorated function into a JSON schema —
# { "name": "add", "description": "Add two numbers...", "parameters": { "a": { "type": "number" }, "b": { "type": "number" } } }

from lanchain_core.tools import tool
import math

@tool
def add(a: float, b: float) -> float:
    """Add two numbers. Use for addition operations."""
    return a + b

@tool
def subtract(a: float, b: float) -> float:
    """Subtract two numbers. Use for subtraction operations."""
    return a - b

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers. Use for multiplication operations."""
    return a * b

@tool
def divide(a: float, b: float) -> float:
    """Divide the first by the second. Use for division operations."""
    return a / b

@tool
def square_root(a: float) -> float:
    """Compute the square root of a number. Use for square root operations."""
    return math.sqrt(a)

tools = [add, subtract, multiply, divide, square_root]

# ------------------------
# STEP 3: Create the Agent
# ------------------------

# create_agent builds a full ReAct loop
# Reason -> Act (call tool) -> Observe -> Repeat 

from langchain.agents import create_agent

agent = create_agent(
	model = model,
	tools = tools
)


# ------------------------
# STEP 4: Run the Agent
# ------------------------
def run_agent(question: str):
     """Run the agent on a question and print the execution trace."""
     print(f"👤 User: {question}")
     print("-"*50)

     result = agent.invoke({
          "messages": [("user", question)]
     })

     print(f"🤖 Agent: {result['output']}")
     print("-"*50)


#simple
run_agent("What is 42 + 58?")

#medium: multiple tool call in sequence 
run_agent("What is 15 multiplied by 8, then divided by 3?")

#complex: the agent must plan a multi-step approach
run_agent("I have a rectangle with width 12 and height 7. What is its area, and what is the square root of that area?")	


import os, json
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic

from personas import persona_one, persona_two, persona_three

# Load environment variables from .env file
load_dotenv()

# Ensure the ANTHROPIC_API_KEY is set in the environment
api_key = os.getenv("ANTHROPIC_API_KEY")

model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    temperature=0.7,
)

agent = create_react_agent(
    model=model,
    tools=[],
    prompt=json.dumps(persona_two)
)

def main():
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "tell me a joke"}]},
    )
    print(response["messages"][-1].content)

main()


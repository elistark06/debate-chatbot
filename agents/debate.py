import os, json
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic
from agents.personas import Debater1, Debater2
from agents.rounds.round_one import speech_one, speech_two

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

model = ChatAnthropic(
    model="claude-3-5-sonnet-20241022",
    temperature=0.7,
)

primer = "you are:"

debater1 = create_react_agent(
    model=model,
    tools=[],
    prompt=json.dumps(Debater1)
)

debater2 = create_react_agent(
    model=model,
    tools=[],
    prompt=json.dumps(Debater2)
)

def debate():
    
    round_one_result = speech_one(model, debater1, True)
    round_two_result = speech_two(model,debater2, False)

    return round_one_result, round_two_result


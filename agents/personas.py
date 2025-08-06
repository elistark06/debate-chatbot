import json
from langgraph.prebuilt import create_react_agent
from agents.rounds.shared import load_markdown_file

with open('debate-data/example.json', 'r') as file:
    debateData = json.load(file)
    debaters = debateData['debaters']

Debater1 = debateData['debaters']['one']
Debater2 = debateData['debaters']['two']
Topic = debateData['debate']['topic']


def init_judges(model):
    markdownFilepath = "debate-data/round-one-judging-instructions.md"
    judgesPrompt = load_markdown_file(markdownFilepath)

    j1Spice = "You are a young woman who grew up middle class in the United states, you will be judging a debate. Try to be unbiased, but stay in your role"
    j2Spice = "You are a older man who teaches highschool in the United Sates, you will be judging a debate. Try to be unbiased, but stay in your role"
    j3Spice = "You are an extremely smart young adult male, and are an experienced debater. You are very smart for your age. You will be judging a debate. Try to be unbiased, but stay in your role"

    judge1 = create_react_agent(
        model=model,
        tools=[],
        prompt=j1Spice+judgesPrompt
    )

    judge2 = create_react_agent(
        model=model,
        tools=[],
        prompt=j2Spice+judgesPrompt
    )

    judge3 = create_react_agent(
        model=model,
        tools=[],
        prompt=j3Spice+judgesPrompt
    )

    return(judge1, judge2, judge3)
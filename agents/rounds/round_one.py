from agents.rounds.shared import load_markdown_file
from agents.personas import Topic
from langgraph.prebuilt import create_react_agent


def initJudges(model):
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

speeches_prompt = "You will write a speech about the given topic. from the perspective you were previously instructed with. Here is the topic:"

def speech_one(model, debater, agrees):

    judges = initJudges(model)

    if agrees:
        stance="you respond from a perspective of agreement, while respecting your persona which should be your initial prompt"
    else:
        stance="you respond from a perspective of disagreemnt, while respecting your persona which should be your intitial prompt"

    speech = debater.invoke(
        {"messages": [{"role": "user", "content": stance+speeches_prompt+Topic}]},
    )

    return speech["messages"][1]

        


def speech_two(model, debater, agrees):

    judges = initJudges(model)

    if agrees:
        stance="you respond from a perspective of agreement, while respecting your persona:"
    else:
        stance="you respond from a perspective of disagreemnt, while respecting your persona:"

    speech = debater.invoke(
        {"messages": [{"role": "user", "content": stance+speeches_prompt+Topic}]},
    )

    return speech["messages"][1]

from agents.personas import Topic


speeches_prompt = "You will write a speech about the given topic. from the perspective you were previously instructed with. Here is the topic:"

def speech_one(debater, agrees):

    if agrees:
        stance="you respond from a perspective of agreement, while respecting your persona which should be your initial prompt"
    else:
        stance="you respond from a perspective of disagreement, while respecting your persona which should be your intitial prompt"

    speech = debater.invoke(
        {"messages": [{"role": "user", "content": stance+speeches_prompt+Topic}]},
    )

    return speech["messages"][-1].content

        


def speech_two(debater, agrees):

    if agrees:
        stance="you respond from a perspective of agreement, while respecting your persona:"
    else:
        stance="you respond from a perspective of disagreemnt, while respecting your persona:"

    speech = debater.invoke(
        {"messages": [{"role": "user", "content": stance+speeches_prompt+Topic}]},
    )

    return speech["messages"][-1].content

from agents.personas import init_judges
from agents.debate import model

def judge_one(speech_one, speech_two):
    
    judges = init_judges(model)

    judge_one_response_one = judges[0].invoke(
        {"messages": [{"role": "user", "content": speech_one}]}
    )

    judge_two_response_one = judges[1].invoke(
        {"messages": [{"role": "user", "content": speech_one}]}
    )

    judge_three_response_one = judges[2].invoke(
        {"messages": [{"role": "user", "content": speech_one}]}
    )

    return judge_one_response_one, judge_two_response_one, judge_three_response_one

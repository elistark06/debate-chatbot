from agents.debate import debate
from agents.judge import judge_one



def judge():
    results = debate()

    speech_one = results[0]
    speech_two = results[1]

    judging = judge_one(speech_one, speech_two)

    return judging

judging_content = judge()

print(judging_content)




    


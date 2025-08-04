import json

with open('debate-data/example.json', 'r') as file:
    debateData = json.load(file)
    debaters = debateData['debaters']

Debater1 = debateData['debaters']['one']
Debater2 = debateData['debaters']['two']
Topic = debateData['debate']['topic']
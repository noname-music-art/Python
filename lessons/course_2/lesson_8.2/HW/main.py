import json
from class_question import *

with open('data/questions.json', encoding='utf-8') as f:
    raw_json = f.read()
    json.loads(raw_json)

questions = []

for question in json.loads(raw_json):
    questions.append(Question(question["q"], int(question["d"]), question["a"]))

for question in questions:
    print(question.build_question())
    question.is_asked = True
    question.user_answer = input()
    print(question.user_answer, question.correct_answer)
    print(question.build_feedback())


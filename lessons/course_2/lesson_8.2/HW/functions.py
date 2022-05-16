# Import functions
import json
import random

# Import Class
from class_question import *


def random_question():
    """
    Gets data from question.json file in folder Data
    store as list of question and return shuffled list
    :return: shuffled(list[Question])
    """
    questions = []

    with open('data/questions.json', encoding='utf-8') as f:
        raw_json = f.read()
        json.loads(raw_json)

    for question in json.loads(raw_json):
        questions.append(Question(question["q"], int(question["d"]), question["a"]))

    random.shuffle(questions)
    return questions


def statistic(questions):
    """
    Gets a list of questions and compiles statistic of correct answers and points earned
    :param questions: list
    :return:
    """
    question_amount = len(questions)
    score = 0
    correct_answers = 0

    for question in questions:
        if question.is_correct():
            score += question.score
            correct_answers += 1
    return f"Вот и всё!\nОтвечено {correct_answers} {ending(correct_answers)} из {question_amount}\n" \
           f"Набрано баллов: {score}"


def ending(correct_answers):
    """
    Gets a numeral and returns a noun with the correct ending
    :param correct_answers: int
    :return: str
    """
    if correct_answers == 0:
        return "вопросов"
    d10 = correct_answers % 10
    d100 = correct_answers % 100
    if d10 == 1 and d100 != 11:
        return "вопрос"
    elif (2 <= d10 <= 4) and (d100 < 10 or d100 > 20):
        return "вопроса"
    else:
        return "вопросов"

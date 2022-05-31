import requests
import random
from basic_word import *


def load_random_word(url):
    """
    Function get random quiz-word from JSON data from Internet.

    :param url: url with JSON data
    :return: exemplar of class BasicWord
    """
    try:
        response = requests.get(url, timeout=1)
        if response.status_code != 200:
            print("Не возможно получить данные для игры. Проверьте URL.")
            exit()
        response_json = response.json()
        quiz_words = []

        for quiz_word in response_json:
            quiz_words.append(BasicWord(quiz_word["word"], quiz_word["subwords"]))

        return random.choice(quiz_words)

    except requests.exceptions.ConnectionError as e:
        print("Не возможно получить данные для игры. Проверьте наличие подключения к Internet")
        quit()
    except requests.exceptions.JSONDecodeError as e:
        print("Мы получили что-то странное, это не похоже JSON")
        quit()
    except requests.exceptions.InvalidSchema as e:
        print("Проверьте правильность указания URL")
        quit()


def ending(correct_answers):
    """
    Gets a numeral and returns a noun with the correct ending

    :param correct_answers: int
    :return: str
    """
    if correct_answers == 0:
        return "слов"
    d10 = correct_answers % 10
    d100 = correct_answers % 100
    if d10 == 1 and d100 != 11:
        return "слово"
    elif (2 <= d10 <= 4) and (d100 < 10 or d100 > 20):
        return "слова"
    else:
        return "слов"

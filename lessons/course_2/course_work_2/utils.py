import requests
import random
from basic_word import *


def load_random_word(url):
    try:
        response = requests.get(url, timeout=1)
        response_json = response.json()
        words = []

        for word in response_json:
            words.append(BasicWord(word["word"], word["subwords"]))

        return random.choice(words)

    except requests.exceptions.ConnectionError as e:
        print("Check your Internet connection")
    except requests.exceptions.JSONDecodeError as e:
        print("Мы получили что-то странное, это не JSON")


    # if response.status_code != 200:
    #     print("Не возможно получить данные для игры. Проверьте URL.")
    #     exit()
    # if response.headers['Content-Type'] != 'application/json':
    #     print("Получены странные данные. Проверьте URL")
    #     exit()




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

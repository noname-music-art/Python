import requests
import random
from basic_word import *


def load_random_word(url):
    response = requests.get(url)
    response_json = response.json()
    words = []

    for word in response_json:
        words.append(BasicWord(word["word"], word["subwords"]))

    return random.choice(words)


word = load_random_word("https://jsonkeeper.com/b/NIAO")
print(word.basic_word, word.allowed_word_list, word.word_count())

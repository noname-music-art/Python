import requests


def load_random_word(url):
    response = requests.get(url)
    response_json = response.json()
    return response_json


print(load_random_word("https://jsonkeeper.com/b/NIAO"))

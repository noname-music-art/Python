import random

user = input("Введите ваше имя : ")

with open("words.txt") as file:
    content = file.read().split("\n")

test = []
score = 0

for word in content:

    word_sh = list(word)
    random.shuffle(word_sh)
    word_sh = "".join(word_sh)
    user_answer = input(f"Угадайте слово: {word_sh}")

    if user_answer == word:
        score += 10
        print("Верно! Вы получаете 10 очков.")
    else:
        print(f"Неверно! Верный ответ – {word}")

with open("history.txt", "at") as file:
    print(file.write(f"{user} {score}\n"))

# with open("history.txt") as file:
#     print()
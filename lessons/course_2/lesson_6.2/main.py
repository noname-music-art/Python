import random

user = input("Введите ваше имя : ")

with open("words.txt") as file:
    content = file.read().split("\n")

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

top_score = []
played_games = 0

with open("history.txt", "rt") as file:
    for stored_data in file:
        played_games += 1
        players, scores = stored_data.rstrip().split(' ')
        top_score.append(scores)

print(f"Total games played: {played_games}")
print(f"Top score: {max(top_score)}")

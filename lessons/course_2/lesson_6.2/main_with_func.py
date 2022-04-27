import random


def get_data_from_file(file_name):
    with open(file_name, "rt") as file:
        content = file.read().split("\n")
    return content


def store_score(user, score):
    with open("history.txt", "at") as file:
        file.write(f"{user} {score}\n")


def shuffle_word(word):
    word_sh = list(word)
    random.shuffle(word_sh)
    word_sh = "".join(word_sh)
    return word_sh


user = input("Enter your name : ")
score = 0

for word in get_data_from_file("words.txt"):

    user_answer = input(f"Guess the word: {shuffle_word(word)} : ")

    if user_answer == word:
        score += 10
        print("Correct! You earn 10 pts.\n")
    else:
        print(f"Wrong! Correct answer – {word}\n")

store_score(user, score)

top_score = []
played_games = 0

for stored_data in get_data_from_file("history.txt"):
    if len(stored_data.split(' ')) == 2:
        players, scores = stored_data.split(' ')
        top_score.append(scores)
        played_games += 1
    else:
        continue

print(f"Total games played: {played_games}")
print(f"Top score: {max(top_score)}")


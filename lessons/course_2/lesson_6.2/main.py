import random

user = input("Enter your name : ")

with open("words.txt") as file:
    content = file.read().split("\n")

score = 0

for word in content:

    word_sh = list(word)
    random.shuffle(word_sh)
    word_sh = "".join(word_sh)
    user_answer = input(f"Guess the word: {word_sh} : ")

    if user_answer == word:
        score += 10
        print("Correct! You earn 10 pts.\n")
    else:
        print(f"Wrong! Correct answer – {word}\n")

with open("history.txt", "at") as file:
    file.write(f"{user} {score}\n")

top_score = []
played_games = 0

with open("history.txt") as file:
    for stored_data in file:
        played_games += 1
        players, scores = stored_data.rstrip().split(' ')
        top_score.append(scores)

print(f"Total games played: {played_games}")
print(f"Top score: {max(top_score)}")

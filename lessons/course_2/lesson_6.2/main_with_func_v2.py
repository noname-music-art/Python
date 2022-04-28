import random


def get_words_from_file(filename):
    with open(filename) as f:
        words_from_file = f.read().split("\n")
    return words_from_file


def shuffle_word(word_to_shuffle):
    shuffled_word = list(word_to_shuffle)
    random.shuffle(shuffled_word)
    shuffled_word = "".join(shuffled_word)
    return shuffled_word


def store_stats_to_file(filename, username, score_count):
    with open(filename, "at") as f:
        f.write(f"{username} {score_count}\n")


def get_stats_from_file(filename):
    played_games = 0
    top_score = []
    with open(filename) as f:
        for stored_data in f:
            played_games += 1
            players, scores = stored_data.rstrip().split(' ')
            top_score.append(scores)

    print(f"Total games played: {played_games}")
    print(f"Top score: {max(top_score)}")


user = input("Enter your name : ")
score = 0

words = get_words_from_file("words.txt")

for word in words:

    user_answer = input(f"Guess the word: {shuffle_word(word)} : ")

    if user_answer == word:
        score += 10
        print("Correct! You earn 10 pts.\n")
    else:
        print(f"Wrong! Correct answer – {word}\n")

store_stats_to_file("history.txt", user, score)

get_stats_from_file("history.txt")

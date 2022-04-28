# Import random for shuffle in shuffle_word function
import random


# Declaring functions
def get_words_from_file(filename):
    """
    Return list of strings from text file

    :param filename: file with data
    :return: list of strings from text file
    """

    with open(filename) as f:
        words_from_file = f.read().split("\n")
    return words_from_file


def shuffle_word(word_to_shuffle):
    """
    Return shuffled word as string

    :param word_to_shuffle: word
    :return: shuffled word as string
    """

    shuffled_word = list(word_to_shuffle)
    random.shuffle(shuffled_word)
    shuffled_word = "".join(shuffled_word)
    return shuffled_word


def store_stats_to_file(filename, username, score_count):
    """
    Store username with score in file

    :param filename: file to save data
    :param username: username
    :param score_count: score
    :return:
    """

    with open(filename, "at") as f:
        f.write(f"{username} {score_count}\n")


def get_stats_from_file(filename):
    """
    Print statistic of played games and hi-score from file

    :param filename: file with stats
    :return:
    """

    played_games = 0
    top_score = []
    with open(filename) as f:
        for stored_data in f:
            played_games += 1
            players, scores = stored_data.rstrip().split(' ')
            top_score.append(scores)

    print(f"Total games played: {played_games}")
    print(f"Top score: {max(top_score)}")


# Get username from user input
user = input("Enter your name : ")

# Set default score
score = 0

# Get words from file by using function "get_words_from_file()"
words = get_words_from_file("words.txt")

# For every word in words:
for word in words:

    # Ask user to input correct word, shuffled with function "shuffle_word()"
    user_answer = input(f"Guess the word: {shuffle_word(word)} : ")

    # If user input correct word, he gains 10 pts and message that he is right
    if user_answer == word:
        score += 10
        print("Correct! You earn 10 pts.\n")
    # If user input incorrect word, he gains message that he is wrong, and correct answer
    else:
        print(f"Wrong! Correct answer – {word}\n")

# Save stats to file with "store_stats_to_file()" function
store_stats_to_file("history.txt", user, score)

# Get and print stats from file with "get_stats_from_file()" function
get_stats_from_file("history.txt")

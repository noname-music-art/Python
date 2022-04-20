# Import choice from random for use in get_word() function
from random import choice


# Definition functions

def morse_encode(word):
    """
    English word to Morse code encoding function

    :param word: - word to encoding
    :return: str - encoded word
    """

    morse_code_dict = {"0": "-----", "1": ".----", "2": "..---", "3": "...--",
                       "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
                       "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
                       "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
                       "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
                       "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", ".": ".-.-.-",
                       ",": "--..--", "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.",
                       "@": ".--.-.", "(": "-.--.", ")": "-.--.-"
                       }

    code_list = []

    for char in word:
        code_list += [morse_code_dict[char]]
    return " ".join(code_list)


def get_word(word_list):
    """
    The function of choosing a random word from a list of words

    :param word_list: list of words to choose from
    :return: str - randomly chosen word
    """

    return choice(word_list)


def print_statistics(answers):
    """
    The function counts and print the number of elements of the list,
    the number of elements True, the number of elements False

    :param answers: - boolean list
    """

    correct_answers = 0
    length = len(answers)

    for answer in answers:
        if answer:
            correct_answers += 1

    keys = ("Всего задачек", "Отвечено верно", "Отвечено неверно")
    values = (length, correct_answers, length - correct_answers)
    result = dict(zip(keys, values))

    for key, item in result.items():
        print(f"{key}: {item}")


# Prepared list of words for training
words_for_training = ["abc", "b", "c"]

# Declaring list for answers
answers = []

# Print welcome and wait for user input to start training
welcome = input("Сегодня мы потренируемся расшифровывать морзянку. \nНажмите Enter и начнем\n")

# Repeat training 3 times
for i in range(1, 4):

    # Get random word from list by get_word() function
    word = get_word(words_for_training)

    # Encode word by morse_encode() function
    encoded_word = morse_encode(word)

    # Print encoded word and get user answer
    get_user_answer = input(f"Слово {i} : {encoded_word}\n")

    # Compare user answer with primal word
    if get_user_answer.lower() == word:

        # Print result for correct answer and store result in answer list
        print(f"Верно, {word.capitalize()}")
        answers += [True]
    else:

        # Print result for wrong answer and store result in answer list
        print(f"Неверно, {word.capitalize()}")
        answers += [False]

# Print result by print_statistics() function
print_statistics(answers)

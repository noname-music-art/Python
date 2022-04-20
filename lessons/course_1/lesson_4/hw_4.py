# Declaration of dictionaries with words of varying complexity.
# Dictionary of easy words.
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}
# Dictionary of medium words.
words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}
# Dictionary of hard words.
words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}
# Declaration dictionary of user level.
levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

# Declaring a variable for the working dictionary.
words = None

# Tuples of names of dictionaries and dictionaries.
available_difficulties = ("легкий", "средний", "сложный")
dict_list = (words_easy, words_medium, words_hard)

# Variable for user input.
get_test_difficult = ()

# User choice of test difficulty.
# Loop repeat until existing complexity is entered.
while not words:

    # Displaying a message and receiving user input.
    get_test_difficult = input("Выберите уровень сложности.\nЛегкий, средний, сложный.\n")

    # Check that the selected difficulty exists. Case insensitive.
    if get_test_difficult.lower() in available_difficulties:

        # Getting a working dictionary and displaying a message about the selected difficulty.
        words = dict_list[available_difficulties.index(get_test_difficult.lower())]
        print(f"Выбран {get_test_difficult.lower()} уровень, мы предложим 5 слов, подберите перевод.\n")
    else:
        # Displaying a message about a non-existent complexity.
        print(f"Нет уровня сложности {get_test_difficult} сделайте другой выбор")

# Declaring a variable for the answer.
answer = []

# Declaring a variable for the answers dictionary.
answers = None

# Repeating the loop for all elements of the working dictionary.
for word, translate in words.items():

    # Print hint and read the user's answer for each word.
    user_answer = input(f"{word}, {len(translate)} букв, начинается на '{translate[0]}' : ")

    # Checking the correctness of the user's answer. Print result based on answer.
    # Save answer result to list.
    if user_answer.lower() == translate:
        print(f"Верно. {word.capitalize()} — это {translate}.\n")
        answer += [True]
    else:
        print(f"Неверно. {word.capitalize()} — это {translate}.\n")
        answer += [False]

# Getting a dictionary of answers from the keys of a working dictionary and an answer list
answers = dict(zip(words.keys(), answer))

# Declaring a variable for the result counter.
correct_answers = 0

# Print result
# For correct answers
print("Правильно отвечены слова: ")
for k, v in answers.items():
    if v:
        print(k)
        correct_answers += 1

# For wrong answers
print("Неправильно отвечены слова: ")
for k, v in answers.items():
    if not v:
        print(k)

# Print User level dependent on correct answers
print(f"Ваш ранг: {levels[correct_answers]}")

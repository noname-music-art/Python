# Import functions and classes
from utils import *
from player import Player

# Gets random word (exemplar of class BasicWord) from outer world by using function with request
# word = load_random_word("https://jsonkeeper.com/b/NIAO")
word = load_random_word("https://ya.ru")
# Create exemplar of class Player with username
player = Player(input("Input name : "))

# Print welcome word using data from player, then
# print task and rules for player using data from exemplar of class basic_word
print(f"Привет {player.user_name}\n"
      f"Составьте {word.word_count()} слов из слова \"{word.basic_word}\"\n"
      f"Слова должны быть не короче 3 букв\n"
      f"Что бы остановить игру введите \"stop\" или \"стоп\"\n"
      f"Поехали, ваше первое слово?\n")

# For allowed number of words
for step in range(0, word.word_count()):

    # Read user answer and store it into exemplar of basic_word
    word.user_word = input("Введите слово : ")

    # Check for stop-word and print result if game stopped
    if word.user_word.lower() == "стоп" or word.user_word.lower() == "stop":
        print(f"Игра завершена!\n"
              f"Вы угадали {player.correct_words()} {ending(player.correct_words())}!")
        exit()

    # Check the word for double usage by class method
    elif player.check_word(word.user_word.lower()):
        print("Вы уже называли это слово")

    # Checking the word for presence in the list of allowed
    elif word.word_check():

        # Add word to list of correct words and return feedback
        player.add_word(word.user_word.lower())
        print("Верно")

    # Return feedback if user word is incorrect
    else:
        print("Неверно")

# Print statistic for player at the end of the game
print(f"Слова закончились, игра завершена!\n"
      f"Вы угадали {player.correct_words()} {ending(player.correct_words())}!")

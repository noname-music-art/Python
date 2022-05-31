# Import functions and classes
from utils import *
from player import Player

# Gets random word (exemplar of class BasicWord) from outer world by using function with request
quiz_word = load_random_word("https://jsonkeeper.com/b/NIAO")

# Create exemplar of class Player with username
player = Player(input("Input name : "))

# Print welcome word using data from player, then
# print task and rules for player using data from exemplar of class BasicWord
print(f"Привет {player.user_name}\n"
      f"Составьте {quiz_word.sub_word_count()} слов из слова \"{quiz_word.basic_word}\"\n"
      f"Слова должны быть не короче 3 букв\n"
      f"Что бы остановить игру введите \"stop\" или \"стоп\"\n"
      f"Поехали, ваше первое слово?\n")

# For allowed number of words
for step in range(0, quiz_word.sub_word_count()):

    # Read user answer
    user_word = input("Введите слово : ").lower()

    # Check for stop-word and print result if game stopped
    if user_word == "стоп" or user_word == "stop":
        print(f"Игра завершена!\n"
              f"Вы угадали {player.correct_words()} {ending(player.correct_words())}!")
        exit()

    # Check the word for double usage by class Player method
    elif player.check_word_in_used(user_word):
        print("Вы уже называли это слово")

    # Checking the word for presence in the list of allowed by class BasicWord method
    elif quiz_word.word_check_in_allowed(user_word):

        # Add word to list of correct and list of used words and return feedback
        player.add_word(user_word, True)
        print("Верно")

    else:
        # Add word to list of used words and return feedback
        player.add_word(user_word, False)
        print("Неверно")

# Print statistic for player at the end of the game
print(f"Слова закончились, игра завершена!\n"
      f"Вы угадали {player.correct_words()} {ending(player.correct_words())}!")

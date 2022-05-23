from utils import *
from player import Player

word = load_random_word("https://jsonkeeper.com/b/NIAO")

player = Player(input("Input name : "))

print(f"Привет {player.user_name}\n"
      f"Составьте {word.word_count()} слов из слова \"{word.basic_word}\"\n"
      f"Слова должны быть не короче 3 букв\n"
      f"Поехали, ваше первое слово?\n")

for step in range(0, word.word_count()):

    word.user_word = input("Введите слово : ")

    if word.user_word == "стоп" or word.user_word == "stop":
        print(f"Игра завершена!\n"
              f"Вы угадали {player.correct_words()} {ending(player.correct_words())}!")
        exit()

    elif player.check_word(word.user_word):
        print("Вы уже называли это слово")

    elif word.word_check():
        player.add_word(word.user_word)
        print("Верно")

    else:
        print("Неверно")

print(f"Слова закончились, игра завершена!\n"
      f"Вы угадали {player.correct_words()} {ending(player.correct_words())}!")

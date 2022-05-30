class Player:

    def __init__(self, user_name):
        self.user_name = user_name
        self.used_words = []

    def correct_words(self):
        return len(self.used_words)

    def add_word(self, user_word):
        self.used_words.append(user_word)

    # проверка использования данного слова до этого (возвращает bool)
    def check_word(self, user_word):
        return user_word in self.used_words

class Player:

    def __init__(self, user_name):
        self.user_name = user_name
        self.used_words = []
        self.correct_user_words = []

    def correct_words(self):
        return len(self.correct_user_words)

    def add_word(self, word_to_add):
        self.used_words.append(word_to_add)

    def check_word(self, word_for_verification):
        return word_for_verification in self.used_words

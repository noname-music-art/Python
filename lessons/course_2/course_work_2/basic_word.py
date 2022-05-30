class BasicWord:

    def __init__(self, basic_word, allowed_word_list):
        self.basic_word = basic_word
        self.allowed_word_list = allowed_word_list
        self.user_word = str

    def word_check(self):
        return self.user_word.lower() in self.allowed_word_list

    def word_count(self):
        return len(self.allowed_word_list)

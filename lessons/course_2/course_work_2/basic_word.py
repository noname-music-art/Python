class BasicWord:

    def __init__(self, basic_word, allowed_word_list):
        self.basic_word = basic_word
        self.allowed_word_list = allowed_word_list
        self.user_word = str

    # проверка введенного слова в списке допустимых под-слов (вернет bool),
    def word_check(self):
        if self.user_word == "стоп" or self.user_word == "stop":
            exit()
        return self.user_word in self.allowed_word_list

    # подсчет количества под-слов (вернет int).
    def word_count(self):
        return len(self.allowed_word_list)

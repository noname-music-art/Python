class BasicWord:
    """Class for quiz-word. Contain functions word_check_in_allowed() and sub_word_count()"""

    def __init__(self, basic_word, allowed_word_list):
        """
        Constructor contain parameters basic word and allowed_word_list

        :param basic_word: string
        :param allowed_word_list: list of strings
        """
        self.basic_word = basic_word
        self.allowed_word_list = allowed_word_list

    def word_check_in_allowed(self, word_to_check_in_allowed):
        """
        Function checks that parameter word_to_check_in_allowed contains in allowed_word_list

        :param word_to_check_in_allowed: string
        :return: bool
        """
        return word_to_check_in_allowed in self.allowed_word_list

    def sub_word_count(self):
        """
        Function count and return allowed words in quiz
        :return: int
        """
        return len(self.allowed_word_list)

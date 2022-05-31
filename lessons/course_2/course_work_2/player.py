class Player:
    """Class Player for users. Contain functions correct_words(), add_word() and check_word_in_used()"""

    def __init__(self, user_name):
        """
        Constructor contain parameter user_name and declares lists of used and correct answers

        :param user_name: string
        """
        self.user_name = user_name
        self.used_words = []
        self.correct_user_words = []

    def correct_words(self):
        """
        Function count and return correct user answers in quiz

        :return: int
        """
        return len(self.correct_user_words)

    def add_word(self, word_to_add, flag):
        """
        Function store the word in the lists of used and correct words (if flag is present)

        :param word_to_add: str
        :param flag: bool
        """
        if flag:
            self.correct_user_words.append(word_to_add)
            self.used_words.append(word_to_add)
        else:
            self.used_words.append(word_to_add)

    def check_word_in_used(self, word_for_verification):
        """
        Function checks if the word has been used before.

        :param word_for_verification: str
        :return: bool
        """
        return word_for_verification in self.used_words

import requests
response = requests.get("https://jsonkeeper.com/b/NIAO")


class BasicWord:
    # Создайте класс `BasicWord` в отдельном файле. Этот класс будет содержать в себе:
    # **Поля:**
    # исходное слово,
    # набор допустимых под-слов.
    # **При инициализации** экземпляру задаются: **исходное слово** и
    # набор **допустимых слов,** составленных из исходного.
    def __init__(self, basic_word, allowed_word_list):
        self.basic_word = basic_word
        self.allowed_word_list = allowed_word_list

    # ** Методы: **
    # - проверку введенного слова в списке допустимых под-слов (вернет bool),
    def word_check(self):
        pass

    # подсчет количества под-слов (вернет int).
    def word_count(self):
        pass

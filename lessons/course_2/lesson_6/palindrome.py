def is_palindrome(word):
    """
    Palindrome test

    :param word: any word
    :return: word == palindrome true or false
    """
    word = word.lower()

    if word == word[::-1]:
        return True
    else:
        return False



def get_record(user_text, start_word='start', stop_word='stop'):
    """

    Function return words between start and stop words

    :param user_text: string of text
    :param start_word: start word (start by default)
    :param stop_word: stop word (stop by default)
    :return: string of text between start and stop
    """
    user_text = user_text.split()

    if start_word in user_text and stop_word in user_text:
        user_text = user_text[user_text.index("start")+1 : user_text.index("stop")]
        return " ".join(user_text)

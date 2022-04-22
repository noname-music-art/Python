def parentheses(formula):
    """

    Bad func not correctly work with ({[)}] and the same

    :param formula:
    :return:
    """
    parentheses_open = ("(", "[", "{")
    parentheses_close = (")", "]", "}")
    check = 0

    for char in formula:
        if char in parentheses_open:
            check += 1
        elif char in parentheses_close:
            check -= 1
        if check < 0:
            return False
    if check != 0:
        return False
    else:
        return True

def roman_to_numerical(code):
    """
    Morse codes to english word encoding function

    :param: code - Morse code to encoding
    :return: str - encoded word
    """
    roman_code_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    dec_list = []

    for char in code:
        for k, v in roman_code_dict.items():
            if char == k:
                dec_list.append(v)

    for index in range(len(dec_list)-1):
        if dec_list[index] < dec_list[index+1]:
            dec_list[index] = -dec_list[index]
    summa = sum(dec_list)
    return summa


print(roman_to_numerical('XXCV'))

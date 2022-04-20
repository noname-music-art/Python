def morse_code_to_word(code):
    """
    Morse codes to english word encoding function

    :param: code - Morse code to encoding
    :return: str - encoded word
    """
    morse_code_dict = {"0": "-----", "1": ".----", "2": "..---", "3": "...--",
                       "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
                       "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
                       "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
                       "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
                       "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", ".": ".-.-.-",
                       ",": "--..--", "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.",
                       "@": ".--.-.", "(": "-.--.", ")": "-.--.-"
                   }

    code_list = []

    code = code.split()

    for char in code:
        for k, v in morse_code_dict.items():
            if char == v:
                code_list += [k]

    print(" ".join(code_list))

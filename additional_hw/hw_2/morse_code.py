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
                       "@": ".--.-.", "(": "-.--.", ")": "-.--.-", " ": " "
                       }

    code_list = []

    code = code.split()

    for char in code:
        for k, v in morse_code_dict.items():
            if char == v:
                code_list += [k]

    return "".join(code_list)


def word_to_morse_code(word):
    """
    English word to Morse code encoding function

    :param: word - word to encoding
    :return: str - encoded word
    """

    morse_code_dict = {"0": "-----", "1": ".----", "2": "..---", "3": "...--",
                       "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
                       "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
                       "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
                       "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
                       "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", ".": ".-.-.-",
                       ",": "--..--", "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.",
                       "@": ".--.-.", "(": "-.--.", ")": "-.--.-", " ": " "
                       }

    code_list = []

    for char in word:
        code_list += [morse_code_dict[char]]
    return " ".join(code_list)


user_input = input()

if user_input.isalpha():
    print(word_to_morse_code(user_input))
else:
    print(morse_code_to_word(user_input))

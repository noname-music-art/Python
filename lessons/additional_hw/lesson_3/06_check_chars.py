# RU and US vowels and punctuation_marks
us_vowels = ["a", "e", "i", "o", "u", "y"]
ru_vowels = ["а", "и", "е", "ё", "о", "у", "ы", "э", "ю", "я"]
punctuation_marks = [".", ",", "...", ":", "?", "!"]

# input Char
char = str(input("Введите знак : "))

# Check is char digit
if char.isdigit():
    print("Это цифра")

# Check is char letter
elif char.isalpha():

    # Check letter for lowercase
    if char.islower():

        # Check is letter vowel or сonsonant
        if char in us_vowels or char in ru_vowels:
            print("Это маленькая гласная")
        else:
            print("Это маленькая согласная")

    # Check uppercase letters
    else:
        # Check is letter vowel or сonsonant
        if char.lower() in us_vowels or char.lower() in ru_vowels:
            print("Это большая гласная")
        else:
            print("Это большая согласная")

# Check is char punctuation mark
elif char in punctuation_marks:
    print("Это знак препинания")

# Print that we don`t know what is it
else:
    print("Это непонятно что")

# Declaring strings of words
dozens = ["ten", "twenty", "thirty", "forthy", "fifty", "sixty", "seventy", "eighty", "ninety"]
units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

# User input
user_number = input("Введите число на английском языке : ")

# Change "-" to spaces for correctly work
corrected_string = user_number.replace("-", " ")

# Getting list of chars from string
spisok = corrected_string.split(" ")

# Checking list length (1 or 2 according to the condition (0..99))
# For 1 elemet
if len(spisok) == 1:

    # Checking element in strings
    # In units
    if spisok[0] in units:
        unit = units.index(spisok[0])
        print(unit)
    # In dozens
    elif spisok[0] in dozens:
        dozen = dozens.index(spisok[0])
        print(f"{dozen + 1}0")
    # In teens
    elif spisok[0] in teens:
        teen = teens.index(spisok[0])
        print(f"1{teen + 1}")
# For 2 elements
elif len(spisok) == 2:
    dozen = dozens.index(spisok[0])
    unit = units.index(spisok[1])
    print(f"{dozen + 1}{unit}")

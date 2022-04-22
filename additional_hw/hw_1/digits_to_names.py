# Declaring strings of words
dozens = ["двадцать", "тридцать", "сорок", "пятьдесят",
    "шестьдесят", "семьдесят", "восемьдесят", "девяносто"
]
units = ["ноль", "один", "два", "три", "четыре",
    "пять", "шесть", "семь", "восемь", "девять"
]
teens = ["десять", "одинадцать", "двенадцать", "тринадцать","четырнадцать",
    "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"
]

# User input
user_number = input("Введите число  : ")

# Getting list of chars from string
new_list = list(str(user_number))

# For numbers < 10
if int(user_number) < 10:
    unit = int(new_list[0])
    print(units[unit])

# For numbers [10..19]
elif 10 <= int(user_number) < 20:
    teen = int(new_list[1])
    print(teens[teen])

# For numbers [20..99]
elif int(user_number) >= 20:
    dozen = int(new_list[0])-2
    unit = int(new_list[1])
    print(f"{dozens[dozen]} {units[unit]}")

else:
    print("Слишком большое число")

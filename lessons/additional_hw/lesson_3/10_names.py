# Declaring lists of names (Comented part to make it easier to check)
serbian = ["Никола", "Лука", "Стефан"]
# , "Марко", "Лазар", "Александр", "Филип", "Йован", "Неманя", "Милош", "Душан"]
kazakh = ["Муртаза", "Меджит", "Ильяс"]
# , "Харун", "Нурадил", "Айрат", "Азиль", "Ерлан"]
yakutian = ["Айхал", "Эркин", "Хорула"]
# , "Уруй", "Дуолан", "Дохсун", "Тимир"]

# Merge names in one list
total_names = serbian + kazakh + yakutian

# Print names from total_names list and read user input
for name in total_names:
    user_answer = input(f"Как вам имя {name} : ")

    # Check for "stop-word"
    if user_answer.lower() == "да":
        print("Отлично, вот мы и выбрали.")
        break

    # Print message that we are starting a new list of names or that names have run out
    if total_names.index(name) == len(serbian) - 1:
        print("Сербские имена закончились. Переходим к казахским!")
    elif total_names.index(name) == len(kazakh + serbian) - 1:
        print("Казахские имена закончились. Переходим к якутским!")
    elif total_names.index(name) == len(kazakh + serbian + yakutian) - 1:
        print("У меня закончились варианты, назовите его новый_сын_1")

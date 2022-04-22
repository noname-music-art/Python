# Declaring lists of names
serbian = ["Никола", "Лука", "Стефан", "Марко", "Лазар", "Александр", "Филип", "Йован", "Неманя", "Милош", "Душан"]
kazakh = ["Муртаза", "Меджит", "Ильяс", "Харун", "Нурадил", "Айрат", "Азиль", "Ерлан"]
yakutian = ["Айхал", "Эркин", "Хорула", "Уруй", "Дуолан", "Дохсун", "Тимир"]

# Test name input
name = input("Введите имя\n")

# Search name in serbian names list
if name.capitalize() in serbian:
    print("это имя сербское")

# Search name in kazakh names list
elif name.capitalize() in kazakh:
    print("это имя казахское")

# Search name in yakutian names list
elif name.capitalize() in yakutian:
    print("это имя якутское")

# Name not found in lists
else:
    print("такого имени нет")

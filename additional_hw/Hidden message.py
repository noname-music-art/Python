dict_to_replace = {"3": "Е", "4": "Ч", "6": "Б", "8": "В", "9": "Д", "0": "О"}
message = 'Мн3 4у9ится, 4т0 кт0-т0 4итает с006щения!!! М0ж3т я 8се при9умала, н0 6у9ь на43ку, 0к?'

for k, v in dict_to_replace.items():
    message = message.replace(k, v)

print(message)

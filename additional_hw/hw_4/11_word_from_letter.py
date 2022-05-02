def ending(num):
    if num == 0:
        return "слов"
    d10 = num % 10
    d100 = num % 100
    if d10 == 1 and d100 != 11:
        return "слово"
    elif (2 <= d10 <= 4) and (d100 < 10 or d100 > 20):
        return "слова"
    else:
        return "слов"


words = ("офицер", "персей", "плюсна", "подруб", "подряд", "полиол", "популо",
         "свекла", "сизетт", "синьор", "усилие", "утенок"
         )

letters = {}

for word in words:
    if not word[0] in letters.keys():
        letters[word[0]] = 1
    else:
        letters[word[0]] += 1

for key, value in letters.items():
    print('{} - {} {}'.format(key.capitalize(), value, ending(value)))

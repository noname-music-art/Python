def remove_from_string(string, *symbols_to_remove):

    for symbol in symbols_to_remove:
        string = string.replace(symbol, "")
    return string


text = ("Если «если» перед «после», значит «после» после «если». Если «если» перед «после», значит «после» после «если».")

clear_string = remove_from_string(text, ",", "«", "»", ".").split(' ')

words = {}

for word in clear_string:
    if word not in words.keys():
        words[word] = 1
    else:
        words[word] += 1

for key, value in words.items():
    print('{}: {}'.format(key, value))

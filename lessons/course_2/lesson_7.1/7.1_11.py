def convert_key(old_key, old_value):
    if old_key == "skolko":
        n_key = "count"
        n_value = int(old_value)
    elif old_key == "poroda":
        n_key = "specie"
        n_value = old_value.capitalize()
    else:
        n_key = "avg_size"
        n_value = int(old_value/10)
    return n_key, n_value

order = [
    {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
    {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
    {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []

for item in order:
    dict_ = {}
    for k, v in item.items():
        new_key, new_value = convert_key(k, v)
        dict_[new_key] = new_value
    order_converted.append(dict_)

for item in order_converted:
    for key, value in item.items():
        print(key, value)

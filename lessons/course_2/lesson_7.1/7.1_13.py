fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]


def get_fish(fish_name):
    for dict_ in fish:
        if fish_name in dict_["specie"]:
            return dict_["specie"], dict_["water"]


fish_name = input()
fish, water = get_fish(fish_name)
print(fish, water)

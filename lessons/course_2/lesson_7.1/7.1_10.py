species = [
{"specie": "Лещ", "len": "29", "sea": False, "desc": "Единственный представитель рода лещей из семейства карповых."},
{"specie": "Щука", "len": "45", "sea": False, "desc": "Распространена в пресных водах Евразии и Северной Америки. Живёт обычно в прибрежной зоне, в водных зарослях, в непроточных или слабопроточных водах."},
{"specie": "Треска", "len": "33", "sea": True, "desc": "Треска встречается от прибрежной полосы до континентального шельфа, но в открытом море над большими глубинами редко. Её жизненный цикл привязан к морским течениям Северной Атлантики."},
{"specie": "Камбала", "len": "25", "sea": True, "desc": "Тело плоское, сильно сжато с боков, глаза расположены не по бокам головы, а смещены на одну её сторону. Плавательного пузыря нет."},
{"specie": "Лосось", "len": "50", "sea": False, "desc": "Проходная форма обитает в северной части Атлантического океана. Заходит на нерест в реки от Португалии и Испании до Баренцева моря."},
]

s = input()
fish_exist = False

for fish in species:
    if fish["specie"] == s:
        fish_exist = True
        print(f'{fish["specie"]}: {fish["desc"]}')
        if fish["sea"]:
            print("Морская рыба")
        else:
            print("Пресноводная рыба")
        print(f'Промысловый размер: {fish["len"]} см')
if not fish_exist:
    print("Информация не найдена")
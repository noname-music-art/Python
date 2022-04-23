track_list = ("Galibri & Mavik – Федерико Феллини", "DaBro - На Часах Ноль-Ноль",
              "Dead Blonde – Мальчик На Девятке", "Султан Лагучев - Горький Вкус",
              "NK – Красное Вино", "Dead Blonde - Бесприданница",
              "Клава Кока & Руки Вверх - Нокаут", "Minelli - Rampampam",
              "Хабиб feat. DJ Smash - Беги", "Асия & Аня Pokrov - Любовь С Картинки",
              "Артём Пивоваров - Рандеву", "Хабиб - Грустинка",
              "Konfuz - Ратата", "Amri - Звезда Тик-Ток", "Konfuz - Ратата", "Amri - Звезда Тик-Ток",
              "Ваня Дмитриенко - Венера-Юпитер", "Galibri & Mavik - Федерико Феллини (Pitched Version)",
              "NLO - Не Грусти")

played_songs = {}

for song in track_list:
    if song not in played_songs.keys():
        played_songs[song] = 1
    else:
        played_songs[song] += 1

for key, value in played_songs.items():
    print('{}: {}'.format(key, value))

workers = {"Мария А": "Фронтендер", "Алексей А": "Фронтендер", "Иван Б": "Бэкендер",
           "Тоня И": "Бэкендер", "Дарья У": "Тестировщик", "Валерия К": "Бэкендер"}

request_profession = input()

for name, profession in workers.items():
    if request_profession == profession:
        print(f"{name}", end=' ')

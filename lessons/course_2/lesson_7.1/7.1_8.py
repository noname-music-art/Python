employees = [

    {"fio": "Киселёв Всеволод Эдуардович ", "vaccinated": True},
    {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
    {"fio": "Аверин Мартын Егорович", "vaccinated": True},
    {"fio": "Князева Августа Егоровна", "vaccinated": False},
    {"fio": "Шанская Аграфена Семеновна", "vaccinated": True},
    {"fio": "Куприна Марина Викторовна", "vaccinated": False},
    {"fio": "Селезнев Константин Игоревич", "vaccinated": False},
]

vaccinated = []
not_vaccinated = []

for employee in employees:
    if employee["vaccinated"]:
        vaccinated.append(employee)
    else:
        not_vaccinated.append(employee)

print(f"Вакцинированные:")
for people in vaccinated:
    print(people["fio"])
print(f"Остальные:")
for people in not_vaccinated:
    print(people["fio"])

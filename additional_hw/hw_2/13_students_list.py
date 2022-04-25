students = {"Мария А.": 55, "Алексей А.": 78, "Иван Б.": 82,
            "Тоня И.": 79, "Дарья У.": 62, "Валерия К.": 69,
            "Дарья Упс.": 71
            }

accepted_students = {}
denied_students = {}

accept_grade = int(input("Введите проходной балл : "))

for student, grade in students.items():
    if grade > accept_grade:
        accepted_students[student] = grade
    else:
        denied_students[student] = grade

if accepted_students:
    print("Поступили :")
    for key in accepted_students:
        print(key)
if denied_students:
    print("Не поступили :")
    for key in denied_students:
        print(key)

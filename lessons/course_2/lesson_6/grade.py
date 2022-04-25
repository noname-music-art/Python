def get_grade(grade):

    grades = {2: "Плохо", 3: "Удовлетворительно", 4: "Хорошо", 5: "Отлично"}
    if grade in grades.keys():
        return grades[grade]
    else:
        return "Ошибка"



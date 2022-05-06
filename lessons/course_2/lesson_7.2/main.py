from functions import get_student_by_pk
from functions import get_profession_by_title
from functions import check_fitness


pk = int(input("Введите номер студента\n"))

student_name, student_skills = get_student_by_pk(pk)

print(f"Студент {student_name}\nЗнает: {', '.join(student_skills)}")

title = input(f"Выберите специальность для оценки студента {student_name}\n")

profession_skills = get_profession_by_title(title)

fitness = check_fitness(student_skills, profession_skills)

print(f"{int(fitness['fit_percent'])}%\n"
      f"{student_name} знает {', '.join(fitness['has'])}\n"
      f"{student_name} не знает {', '.join(fitness['lacks'])}")

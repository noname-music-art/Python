# Import functions
from functions import get_student_by_pk
from functions import get_profession_by_title
from functions import check_fitness

# Input student ID
try:
    pk = int(input("Введите номер студента\n"))
except ValueError:
    print("Допускается ввод только в цифровом формате")
    quit()

# get student name and skills by id
student_name, student_skills = get_student_by_pk(pk)

# print student name and skills
print(f"Студент {student_name}\nЗнает: {', '.join(student_skills)}")

# input profession title for check student fitnesse
title = input(f"Введите специальность для оценки студента {student_name} "
              f"или наберите /help для получения списка доступных специальностей\n")

# get profession skills by title
profession_skills = get_profession_by_title(title.capitalize())

# get the result of the student's compliance with the profession with relevant skills
fitness = check_fitness(student_skills, profession_skills)

# print summary results
print(f"{int(fitness['fit_percent'])}%\n"
      f"{student_name} знает {', '.join(fitness['has'])}\n"
      f"{student_name} не знает {', '.join(fitness['lacks'])}")

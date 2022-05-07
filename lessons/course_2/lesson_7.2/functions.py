import json


def load_students():
    """
    Load data from students.json
    :return: strings from students.json
    """
    with open('data/students.json') as f:
        raw_json = f.read()
    return json.loads(raw_json)


def load_professions():
    """
    Load data from professions.json
    :return: strings from profession.json
    """
    with open('data/professions.json') as f:
        raw_json = f.read()
    return json.loads(raw_json)


def get_student_by_pk(pk):
    """
    Returns student name and student skills as tuple by student ID
    :param pk: student ID
    :return: tuple of values student_name and list of students_skills
    """
    students = load_students()
    for i in range(0, len(students)):
        if pk == students[i]['pk']:
            student_name = students[i]['full_name']
            student_skills = students[i]['skills']
            return student_name, student_skills
    print("У нас нет такого студента")
    quit()


def get_profession_by_title(title):
    """
    Returns profession skills by profession title.
    :param title: title of profession
    :return: list of profession skills
    """
    professions = load_professions()
    for i in range(0, len(professions)):
        if title == professions[i]['title']:
            return professions[i]['skills']
    print("У нас нет такой специальности")
    quit()


def check_fitness(student, profession):
    """
    Returns a dictionary of student skill suitability and job requirements.
    :param student: list of student skills
    :param profession: list of profession requirements
    :return: dictionary of suitability
    """
    fitness = {}
    student_skills = set(student)
    profession_skills = set(profession)
    fitness['has'] = student_skills.intersection(profession_skills)
    fitness['lacks'] = profession_skills.difference(student_skills)
    fitness['fit_percent'] = len(fitness['has']) / len(profession_skills) * 100
    return fitness

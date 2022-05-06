import json


def load_students():
    """

    :return:
    """
    with open('data/students.json') as f:
        raw_json = f.read()
    return json.loads(raw_json)


def load_professions():
    """

    :return:
    """
    with open('data/professions.json') as f:
        raw_json = f.read()
    return json.loads(raw_json)


def get_student_by_pk(pk):
    """

    :param pk: 
    :return: 
    """
    students = load_students()

    student_name = students[pk-1]['full_name']
    student_skills = students[pk - 1]['skills']
    return student_name, student_skills


def get_profession_by_title(title):
    """

    :param title:
    :return:
    """
    professions = load_professions()

    for i in range(0, len(professions)):
        if title in professions[i]['title']:
            return professions[i]['skills']


def check_fitness(student, profession):
    fitness = {}
    student_skills = set(student)
    profession_skills = set(profession)
    fitness['has'] = student_skills.intersection(profession_skills)
    fitness['lacks'] = profession_skills.difference(student_skills)
    fitness['fit_percent'] = len(fitness['has']) / len(profession_skills) * 100
    return fitness

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

    return students[pk-1]


def get_profession_by_title(title):
    """

    :param title:
    :return:
    """
    professions = load_professions()
    for i in range(0, len(professions)):
        if title in professions[i]['title']:
            return professions[i]['skills']


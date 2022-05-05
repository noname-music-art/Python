from functions import load_students
from functions import load_professions
from functions import get_student_by_pk
from functions import get_profession_by_title


students = load_students()
professions = load_professions()

print(get_student_by_pk(1))

print(get_profession_by_title('Frontend'))

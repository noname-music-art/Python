# Declaring lists of question
questions = [
    "Два кружочка рядом встали — Что за дивные очки? Поверни хоть вверх ногами, Одинаковы они!",
    "Лебедь плавает в тетрадке, Значит что-то не в порядке. Если ты совсем Незнайка, Цифру эту получай-ка.",
    "Цифра эта так хитра, Ты её переверни, И начнутся чудеса — Цифру шесть увидишь ты!",
    "Она похожа на топор, Но не колит дров во двор. Как коса, но не совсем, Просто это цифра…",
    "Палочка, но с завитком, Как кочерга — такая же на вид. Эта цифра первая во всём, И в счёте впереди других стоит!"
]

# Declaring lists of answers
answers = ["восемь", "два", "девять", "семь", "один"]

# User input for select question
counter = int(input("Введите цифру от 1 до 5 для выбора загадки "))-1

# User input for select question
answer = input(f"Отгадайте загадку '{questions[counter]}'\n")

# If user answer correct print "Correct"
if answer.lower() == answers[counter]:
    print("Ответ верный")
# If user answer incorrect print "Incorrect" and "Correct answer is ... "
else :
    print(f"Ответ неверный. Верный ответ: {answers[counter].title()}")
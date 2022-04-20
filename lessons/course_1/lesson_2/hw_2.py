#Program Eng_test.
#Some elements in the code were added only to improve the appearance in console like \n and endings
#Comment access granted, you can leave comments right here. =)

#Declaring variables
correct_answers_counter = 0

#Declaring constants
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
correct_answers = ["is","am","in"]
endings = ['ов', '', 'а', 'а']

#Greeting and username input
user_name = input("Привет! Предлагаю проверить свои знания английского! Расскажи, как тебя зовут! ")
print(f"Привет, {user_name}, начинаем тренировку!\n")

#Output tasks, get answers, checking answers, output of intermediate results
for elements in questions:
    print(elements)
    answer = input("Вставьте пропущеное слово : ")
    if answer == correct_answers[questions.index(elements)]:
        correct_answers_counter += 1
        print(f'''Ответ верный! \nВы получаете 10 баллов!\n''')
    else:
        print(f'''Неправильно. \nПравильный ответ: {correct_answers[questions.index(elements)]}\n''')

#Output final results. Ammount of correct answers, score and percentage of correct answers.
print(f'''Вот и все, {user_name}!

Вы ответили на {correct_answers_counter} вопрос{endings[correct_answers_counter]} из 3 верно.
Вы заработали {correct_answers_counter*10} баллов.
Это {round(correct_answers_counter/3*100, 2)}%.''')

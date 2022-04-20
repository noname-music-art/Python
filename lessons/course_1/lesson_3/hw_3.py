# Program Eng_test rev.0.3
# Notes on past homework are taken into. The line of endings has been replaced with a function
# Comment access granted, you can leave comments right here. =)

# Function for insert correct endings in results.
def ending(num):
    if num == 0:
        return "ов"
    d10 = num % 10
    d100 = num % 100
    if d10 == 1 and d100 != 11:
        return ""
    elif (2 <= d10 <= 4) and (d100 < 10 or d100 > 20):
        return "а"
    else:
        return "ов"


# Declaring variables

# Correct answer counter
correct_answers_counter = 0

# Total score counter
total_score = 0

# Declaring constants. String "questions" must be same lenght as "correct_answers".
# Tested for correctly work for more than 3 elements (4) =).

# String of questions
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]

# String of answers
correct_answers = ["is", "am", "in"]

# Greeting and ready check

# Read "Ready" for start
ready_check = input('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать! ')

# Else not necessery i think but colab didn`t correctly work with "exit()"
# We can just put exit(0) in if
# Uses .lower() to properly recognize uppercase input and mixed input
if not ready_check.lower() == "ready":
    print(f"Кажется, вы не хотите играть. Очень жаль.\n")
else:

    # Username input
    # I leave greeting from previous homework, but i can drop it if it`s necessery
    user_name = input("Представьтесь пожалуйста ")
    print(f"Давай приступим к тренировке, {user_name}!\n")

    # Output task and read answer for 1st time for every elemet in string question
    for elements in questions:
        print(elements)
        answer = input("Вставьте пропущеное слово : ")

        # Repeat question for 3 times for every question if aswer is wrong or end cycle if answer is correct
        for attempts_count in range(3, 0, -1):

            # If we got correct answer. Uses .lower() for properly recognize in uppercase or mixed input
            if answer.lower() == correct_answers[questions.index(elements)]:

                # Increas correct answers counter
                correct_answers_counter += 1

                # Print the result depending on the attempts spent
                print(f'''Ответ верный! \nВы получаете {attempts_count} балл{ending(attempts_count)}!\n''')

                # Store total score counter
                total_score += attempts_count

                # Interrupt cycle
                break

            # If we got the wrong answer and we have attempts left, print attempts counter and read new input
            elif attempts_count > 1:
                print(f'''Неправильно. \nОсталось попыток: {attempts_count - 1}, попробуйте ещё раз\n''')
                answer = input("Вставьте пропущеное слово : ")

            # If we got the wrong answer and we have no attempts left, print sorry and correct answer
            else:
                print(f'''Увы, но нет. \nВерный ответ: {correct_answers[questions.index(elements)]}\n''')

    # Output final results. Ammount of correct answers, score and percentage of max score.
    # I print statistics not from the correct answers, but from the maximum possible number of points.
    # It seemed to me so much better. =)
    print(f'''Вот и все, {user_name}!

Вы ответили на {correct_answers_counter} вопрос{ending(correct_answers_counter)} из {len(questions)} верно.
Вы заработали {total_score} балл{ending(total_score)}.
Это {round(total_score / (len(questions) * 3) * 100, 2)}% от максимального количества баллов''')

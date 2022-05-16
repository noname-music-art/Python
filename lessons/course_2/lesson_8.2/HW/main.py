# Import functions
from functions import *

# Get shuffled questions
questions = random_question()

# Asks a questions to the user, gets the user's answer for each question,
# marks them as asked, checks and prints feedback with a preliminary result.
for question in questions:

    # Ask question
    print(question.build_question())

    # Get user answer
    user_answer = input()
    question.user_answer = user_answer

    # Mark question as asked
    question.is_asked = True

    # Print feedback on user answer
    print(question.build_feedback())

# Print statistic for all questions
print(statistic(questions))

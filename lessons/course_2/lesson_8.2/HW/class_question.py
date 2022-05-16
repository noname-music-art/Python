class Question:
    """ Class Question. Contains fields:
    - question text
    - the complexity of the question
    - correct answer
    - is a question asked (false by default)
    - user response (None by default)
    - points per question (Depend on complexity(difficult*10))
    """
    def __init__(self, question, difficult, correct_answer):
        self.question = question
        self.difficult = difficult
        self.correct_answer = correct_answer
        self.is_asked = False
        self.user_answer = None
        self.score = self.difficult*10

    def get_points(self):
        """Return int, score count. Depends on difficult"""
        return self.score

    def is_correct(self):
        """Return Bool. Compares the user's answer with the correct answer"""
        return self.user_answer == self.correct_answer

    def build_question(self):
        """Makes and return user-friendly view of question"""
        return f"Вопрос: {self.question} \nСложность {self.difficult}/5"

    def build_feedback(self):
        """Makes a feedback on user answer"""
        if self.is_correct():
            return f"Ответ верный, получено {self.score} баллов"
        return f"Ответ неверный, верный ответ {self.correct_answer}"

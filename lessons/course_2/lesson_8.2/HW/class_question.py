class Question:
    def __init__(self, question, difficult, correct_answer):
        self.question = question
        self.difficult = difficult
        self.correct_answer = correct_answer
        self.is_asked = False
        self.user_answer = None
        self.score = self.difficult*10

    def get_points(self):
        return self.score

    def is_correct(self):
        return self.user_answer == self.correct_answer

    def build_question(self):
        return f"Вопрос: {self.question} \nСложность {self.difficult}/5"

    def build_feedback(self):
        if self.is_correct:
            return f"Ответ верный, получено {self.score} баллов"
        return f"Ответ неверный, верный ответ {self.correct_answer}"

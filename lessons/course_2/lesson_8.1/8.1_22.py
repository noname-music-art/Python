class Number:

    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def add(self, value):
        self.value += value

    def subtract(self, value):
        self.value -= value


# Не удаляйте этот код, он нужен для проверки

n = Number(7)
print(n.get())
n.add(3)
print(n.get())
n.subtract(5)
print(n.get())

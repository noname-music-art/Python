class Hero():

    def __init__(self, name, posessions):
        self.name = name
        self.posessions = posessions

    def __repr__(self):
        return f'Герой {self.name}. При себе имеет {", ".join(self.posessions)}'


hero = Hero("Питомир", ["меч", "плащ", "шляпа"])


print(hero)
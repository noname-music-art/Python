class Hero:

  def go_right(self, distance):
    print(f"Я иду {distance} метров направо")

  def go_left(self, distance):
    print(f"Я иду {distance} метров налево")

  def observe(self):
    print("Я осматриваюсь")


hero = Hero()

hero.go_right(50)
hero.go_left(30)
hero.observe()

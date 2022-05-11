class Ticket:

    def __init__(self, flight, class_):  # нельзя использовать переменную class
        self.flight = flight
        self.class_ = class_

    def print(self):  # а вот принт - можно, ведь методы не конфликтуют с фукциями!
        print(f"Я билетик на рейс {self.flight} в класс {self.class_}")


ticket_1 = Ticket("SP-101", "econom")
ticket_1.print()

# '''========================================================'''

class Ticket:

    def __init__(self, flight, class_):  # нельзя использовать переменную class
        self.flight = flight
        self.class_ = class_

    def print(self):  # а вот принт - можно, ведь методы не конфликтуют с фукциями!
        print(f"Я билетик на рейс {self.flight} в класс {self.class_}")


ticket_2 = Ticket("PD-320", "econom")
ticket_2.print()
ticket_2.class_ = "business"
ticket_2.print()

# '''========================================================'''

class Ticket:

    def __init__(self, flight, seat_class):  # нельзя использовать переменную class
        self.flight = flight
        self.seat_class = flight

    def print(self):  # а вот принт - можно, ведь методы не конфликтуют с фукциями!
        print(f"Я билетик на рейс {self.flight} в класс {self.seat_class}")


ticket_1 = Ticket("PD-320", "econom")
ticket_2 = Ticket("SP-101", "econom")

tickets = [ticket_1, ticket_2]

for ticket in tickets:
    ticket.print()

# '''========================================================'''

class Ticket():

    def __init__(self, flight, seat_class):  # нельзя использовать переменную class
        self.flight = flight
        self.seat_class = seat_class

    def print(self):  # а вот принт - можно, ведь методы не конфликтуют с фукциями!
        print(f"Я билетик на рейс {self.flight} в класс {self.seat_class}")


ticket_1 = Ticket("PD-320", "econom")
ticket_2 = Ticket("SP-101", "econom")

tickets = {"Туда": ticket_1, "Обратно": ticket_2}

tickets["Туда"].print()
tickets["Обратно"].print()
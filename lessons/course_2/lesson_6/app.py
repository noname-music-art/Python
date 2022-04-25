from validators.validate_pin import validate_pin
from validators.validate_card import validate_card

card_number = input("Введите ваш номер карты")
card_pin = input("Введите ваш пин-код")

if validate_card(card_number):
    print("Номер карты допустимый")
else:
    print("Номер карты недопустимый")

if validate_pin(card_pin):
    print("Пин код допустимый")
else:
    print("Пин код недопустимый")


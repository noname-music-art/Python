from pin import check_pin

user_input = input("Введите ваш пин-код")

if check_pin(user_input):
    print("Такой пин-код подходит")
else:
    print("Такой пин-код НЕ подходит")


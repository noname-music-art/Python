# User input ticket number
ticket_number = input("Введите номер билетика : ")

# Checking the correct length, continue if True
if len(ticket_number) == 6:

    # Getting slices of left and right half
    left_part = ticket_number[:3]
    right_part = ticket_number[3:]

    # Convert slice values to numbers
    left_num = map(int, left_part)
    right_num = map(int, right_part)

    # Сhecking ticket for luckiness
    if sum(left_num) == sum(right_num):

        # Print result, if ticket is lucky
        print("Это счастливый билетик, ешьте его скорей!")
    else:
        # Print result, if ticket is not lucky
        print("Это обычный билетик, но вы все равно можете его съесть!")
else:
    # Print result, if ticket lenght is incorrect
    print("Это не похоже на номер билетика!")

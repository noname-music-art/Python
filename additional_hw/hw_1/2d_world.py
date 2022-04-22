# Declaring lists of terrain and start position
map_line = ["трава", "камни", "озеро", "озеро", "песок", "камни", "земля"]
pos = 0

# While not brake
while True:

    # Print current position and terrain type. Read move direction.
    move_direction = input(
        f"Вы находитесь на клетке {pos + 1}. Вокруг вас {map_line[pos]}. Куда вы пойдете: вперед или назад? ")

    # If move direction forvard
    if move_direction.lower() == "вперед":

        # If move direction forvard and not end of map change pos
        if pos < len(map_line) - 1:
            pos += 1

        # If move direction forvard and end of map print error
        else:
            print("Там ничего нет, туда идти нельзя.")

    # If move direction backward
    elif move_direction.lower() == "назад":

        # If move direction backward and not end of map change pos
        if pos > 0:
            pos -= 1

        # If move direction backward and end of map print error
        else:
            print("Там ничего нет, туда идти нельзя.")

    # Break cycle if enter "выход"
    elif move_direction.lower() == "выход":
        break

    # Print error if user input not "вперед"/"назад" or "выход"
    else:
        print("Не знаю такой команды. Доступно вперед/назад/выход")

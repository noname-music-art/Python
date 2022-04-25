login = input(f"Введите имя пользователя")
pwd = input(f"Введите пароль")

bad_pass = False

if len(login) <= 3:
    print("Логин должен содержать больше 3 символов.")
    bad_pass = True

if len(pwd) <= 8:
    print("Пароль должен содержать больше 8 символов.")
    bad_pass = True

if pwd.isalpha():
    print("Пароль должен содержать хотя бы одну цифру.")
    bad_pass = True

if not bad_pass:
    print("Это хорошие логин и пароль!")

'''Test'''

free_post = ["yandex.ru", "mail.ru", "gmail.com", "rambler.ru"]
mail = input(f"введите почту")
if "@" not in mail:
    print("Это не почта")
mail = mail.split("@")
if not mail[0]:
    print("Это не почта")
elif mail[1] not in free_post:
    if "." not in mail[1]:
        print("Это не почта")
    mail = mail[1].split(".")
    if not mail[0] and not mail[1]:
        print("Это не почта")
    elif 1 < len(mail[1]) <= 3:
        print("Это корпоративная почта")
else:
    print("Это почта, она на бесплатном домене")

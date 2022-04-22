def phone_numer_replace(user_text):
    word_to_remove = ["+", "-", "(", ")"]

    for char in word_to_remove:
        user_text = user_text.replace(char, "")

    splited_text = user_text.split(' ')

    cleaned_text = ["***" if splited_text.isdigit() else splited_text for splited_text in splited_text]

    print(' '.join(cleaned_text))


text = input()
phone_numer_replace(text)

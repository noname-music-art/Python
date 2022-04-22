# String of words to remove
word_to_remove = ["черный", "черная", "белый", "белая",
                  "зеленый", "зеленая", "зеленое", "красный",
                  "красное", "красной", "рыжий", "рыжая"
                  ]

# Text
text = '''Весь красный от злости, Рыжий Джордж вышел на крыльцо и заорал: “вот грязная черная свинья,
которую нужно пристрелить!” – и действительно, у его красной машины паслась маленькая черная вьетнамская свинья.'''

# Split text for elements
splited_text = text.split(' ')

# Clean text
cleaned_text = ["***" if splited_text in word_to_remove else splited_text for splited_text in splited_text]

# Print result
print(' '.join(cleaned_text))

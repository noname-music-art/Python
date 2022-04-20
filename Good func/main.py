import morse_code_to_word
import word_to_morse_code

word = input()

coded = word_to_morse_code.word_to_morse_code(word)

print(coded)

encoded = morse_code_to_word.morse_code_to_word(coded)

print(encoded)


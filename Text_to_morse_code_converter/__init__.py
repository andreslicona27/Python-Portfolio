from Alphabet import Alphabet


def morse_to_text(morse_code):
    words = morse_code.split(' / ')
    text_message = " "
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in Alphabet.morse_alphabet:
                text_message += Alphabet.morse_alphabet[letter]
        text_message += ' '

    return text_message


def text_to_morse(text):
    morse_code = " "
    for character in text:
        if character == ' ':
            morse_code += '/ '
        else:
            morse_code += Alphabet.inverted_alphabet[character.upper()] + " "

    return morse_code


while True:
    conversion = input("Type your choice: \n 1 Morse to text \n 2 Text to morse \n 3 Exit\n")
    new_message = " "

    if conversion == '1':
        message = input("Write the morse code: ")
        new_message = morse_to_text(message)

    elif conversion == '2':
        message = input("Write the message: ")
        new_message = text_to_morse(message)

    elif conversion == '3':
        break

    print(new_message + "\n")

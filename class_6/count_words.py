def read_message():
    message = ""
    while True:
        character = input("Enter your message, one character at a time, then `.` to stop: ")
        message += character
        if character == ".":
            break
    return message

def count_words(message):
    word_count = 0
    is_space = True

    for character in message:
        if character.isspace():
            is_space = True
        elif character == ".":
            break
        elif is_space:
            word_count += 1
            is_space = False

    return word_count

def main():
    message = read_message()
    word_count = count_words(message)
    print("Number of words in your message:", word_count)

main()
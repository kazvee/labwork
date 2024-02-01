total_a_characters = 0
character_to_check = input("Enter a character, or enter '$' to stop: ")

while character_to_check != '$':
    if character_to_check == 'a':
        total_a_characters += 1
    character_to_check = input("Enter a character, or enter '$' to stop: ")

print("The number of times `a` was entered is: ", total_a_characters, "!", sep='')
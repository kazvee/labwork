totalACharacters = 0
characterToCheck = input("Enter a character, or enter '$' to stop: ")

while characterToCheck != '$':
    if characterToCheck == 'a':
        totalACharacters += 1
    characterToCheck = input("Enter a character, or enter '$' to stop: ")

print("The number of times `a` was entered is: ", totalACharacters, "!", sep='')
lastNumber = None
currentNumber = None

lastNumber = input("Enter a number, or enter '$' to stop: ")

while lastNumber != '$':
    nextNumber = int(lastNumber)

    if currentNumber is not None and currentNumber >= nextNumber:
        print("The numbers are not in increasing order.")
        break

    currentNumber = nextNumber
    lastNumber = input("Enter a number, or enter '$' to stop: ")
else:
    print("The numbers are in increasing order.")
last_number = None
current_number = None

last_number = input("Enter a number, or enter '$' to stop: ")

while last_number != '$':
    nextNumber = int(last_number)

    if current_number is not None and current_number >= nextNumber:
        print("The numbers are not in increasing order.")
        break

    current_number = nextNumber
    last_number = input("Enter a number, or enter '$' to stop: ")
else:
    print("The numbers are in increasing order.")
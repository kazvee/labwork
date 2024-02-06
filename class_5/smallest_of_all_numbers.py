numbers = []

while True:
    user_input = input("Enter a number, or enter '$' to stop: ")

    if user_input == "$":
        break

    if user_input.isdigit():
        numbers.append(int(user_input))

if numbers:
    smallest_number = min(numbers)
    print("The smallest number is:", smallest_number)
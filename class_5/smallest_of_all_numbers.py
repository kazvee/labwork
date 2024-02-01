smallest_number = float('inf')
number_to_check = input("Enter a number, or enter '$' to stop: ")

while number_to_check != '$':
    number_to_check = int(number_to_check)

    if number_to_check < smallest_number:
        smallest_number = number_to_check

    number_to_check = input("Enter a number, or enter '$' to stop: ")

print("The smallest number is:", smallest_number)
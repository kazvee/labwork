numbers = []
number_to_check = int(input("Enter a number, or enter `-1` to stop: "))

while number_to_check != -1:
    numbers.append(number_to_check)
    number_to_check = int(input("Enter a number, or enter `-1` to stop: "))

largest_number = max(numbers)
print("The largest number is: ", largest_number)
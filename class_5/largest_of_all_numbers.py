largest_number = float('-inf')
number_to_check = int(input("Enter a number, or enter `-1` to stop: "))

while number_to_check != -1:
    if number_to_check > largest_number:
        largest_number = number_to_check
    number_to_check = int(input("Enter a number, or enter `-1` to stop: "))

print("The largest number is: ", largest_number)
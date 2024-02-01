largest_number = float('-inf')
position_of_largest_number = 0
current_position_of_largest_number = 0

number_to_check = float(input("Enter a real number, or enter `-1` to stop: "))

while number_to_check != -1:
    current_position_of_largest_number += 1

    if number_to_check > largest_number:
        largest_number = number_to_check
        position_of_largest_number = current_position_of_largest_number
    number_to_check = float(input("Enter a real number, or enter `-1` to stop: "))

print("The largest number is:", largest_number, "and it was at position", position_of_largest_number, "in the list!")
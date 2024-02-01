total_multiples_of_two_or_three = 0
total_between_1_and_100 = 0

number_to_check = input("Enter a number, or enter '$' to stop: ")

while number_to_check != "$":

    if 1 <= int(number_to_check) <= 100:
        total_between_1_and_100 += 1

    if (int(number_to_check) % 2 == 0 or int(number_to_check) % 3 == 0) and not (int(number_to_check) % 2 == 0 and int(number_to_check) % 3 == 0):
        total_multiples_of_two_or_three += 1

    number_to_check = input("Enter a number, or enter '$' to stop: ")

print("The total numbers entered between 1 and 100 are:", total_between_1_and_100)
print("The total numbers which are multiples of two or three are:", total_multiples_of_two_or_three)
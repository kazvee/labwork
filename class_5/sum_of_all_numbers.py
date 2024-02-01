total_sum = 0
number_to_add = int(input("Enter a number, or enter `0` to stop: "))

while number_to_add != 0:
    total_sum += number_to_add
    number_to_add = int(input("Enter a number, or enter `0` to stop: "))

print("The sum of all those numbers is: ", total_sum)
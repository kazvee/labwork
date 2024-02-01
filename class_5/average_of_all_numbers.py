numbers_entered = 0
total_sum = 0
average = 0
number_to_add = int(input("Enter a number, or enter `0` to stop: "))

while number_to_add != 0:
    total_sum += number_to_add
    numbers_entered += 1
    number_to_add = int(input("Enter a number, or enter `0` to stop: "))
average = total_sum / numbers_entered

print("The average of all those numbers is: ", average)
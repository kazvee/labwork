total_between_50_and_60 = 0
total_between_61_and_80 = 0
total_between_81_and_100 = 0

weight_to_check = input("Enter a weight, or enter `$` to stop: ")

while weight_to_check != "$":
    weight_to_check = int(weight_to_check)

    if weight_to_check >= 50 and weight_to_check <= 60:
        total_between_50_and_60 += 1
    elif weight_to_check >= 61 and weight_to_check <= 80:
        total_between_61_and_80 += 1
    elif weight_to_check >= 81 and weight_to_check <= 100:
        total_between_81_and_100 += 1

    weight_to_check = input("Enter a weight, or enter '$' to stop: ")

print("The number of weights between 50 and 60 is: ", total_between_50_and_60)
print("The number of weights between 61 and 80 is: ", total_between_61_and_80)
print("The number of weights between 81 and 100 is: ", total_between_81_and_100)
totalBetween50And60 = 0
totalBetween61And80 = 0
totalBetween81And100 = 0

weightToCheck = input("Enter a weight, or enter `$` to stop: ")

while weightToCheck != "$":
    weightToCheck = int(weightToCheck)

    if weightToCheck >= 50 and weightToCheck <= 60:
        totalBetween50And60 += 1
    elif weightToCheck >= 61 and weightToCheck <= 80:
        totalBetween61And80 += 1
    elif weightToCheck >= 81 and weightToCheck <= 100:
        totalBetween81And100 += 1

    weightToCheck = input("Enter a weight, or enter '$' to stop: ")

print("The number of weights between 50 and 60 is: ", totalBetween50And60)
print("The number of weights between 61 and 80 is: ", totalBetween61And80)
print("The number of weights between 81 and 100 is: ", totalBetween81And100)
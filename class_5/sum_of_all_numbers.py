totalSum = 0
numberToAdd = int(input("Enter a number, or enter `0` to stop: "))

while numberToAdd != 0:
    totalSum += numberToAdd
    numberToAdd = int(input("Enter a number, or enter `0` to stop: "))

print("The sum of all those numbers is: ", totalSum)
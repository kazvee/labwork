numbersEntered = 0
totalSum = 0
average = 0
numberToAdd = int(input("Enter a number, or enter `0` to stop: "))

while numberToAdd != 0:
    totalSum += numberToAdd
    numbersEntered += 1
    numberToAdd = int(input("Enter a number, or enter `0` to stop: "))
average = totalSum / numbersEntered

print("The average of all those numbers is: ", average)
smallestNumber = 9999999999999999999999999999999999999999999999999999999999999
numberToCheck = int(input("Enter a positive number, or enter `-1` to stop: "))

while numberToCheck != -1:
    if numberToCheck < smallestNumber:
        smallestNumber = numberToCheck
    numberToCheck = int(input("Enter a positive number, or enter `-1` to stop: "))

print("The smallest number is:", smallestNumber)
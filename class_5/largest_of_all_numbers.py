largestNumber = float('-inf')
numberToCheck = int(input("Enter a number, or enter `-1` to stop: "))

while numberToCheck != -1:
    if numberToCheck > largestNumber:
        largestNumber = numberToCheck
    numberToCheck = int(input("Enter a number, or enter `-1` to stop: "))

print("The largest number is: ", largestNumber)
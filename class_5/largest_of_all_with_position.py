largestNumber = float('-inf')
positionOfLargestNumber = 0
currentPositionOfLargestNumber = 0

numberToCheck = float(input("Enter a real number, or enter `-1` to stop: "))

while numberToCheck != -1:
    currentPositionOfLargestNumber += 1

    if numberToCheck > largestNumber:
        largestNumber = numberToCheck
        positionOfLargestNumber = currentPositionOfLargestNumber
    numberToCheck = float(input("Enter a real number, or enter `-1` to stop: "))

print("The largest number is:", largestNumber, "and it was at position", positionOfLargestNumber, "in the list!")
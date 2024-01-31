totalMultiplesOfTwoOrThree = 0
totalBetween1And100 = 0

numberToCheck = input("Enter a number, or enter '$' to stop: ")

while numberToCheck != "$":

    if 1 <= int(numberToCheck) <= 100:
        totalBetween1And100 += 1

    if (int(numberToCheck) % 2 == 0 or int(numberToCheck) % 3 == 0) and not (int(numberToCheck) % 2 == 0 and int(numberToCheck) % 3 == 0):
        totalMultiplesOfTwoOrThree += 1

    numberToCheck = input("Enter a number, or enter '$' to stop: ")

print("The total numbers entered between 1 and 100 are:", totalBetween1And100)
print("The total numbers which are multiples of two or three are:", totalMultiplesOfTwoOrThree)
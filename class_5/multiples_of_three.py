numberToCheck = int(input("Enter a number to check how many multiples of 3 there are: "))

amountOfMultiples = 0

for number in range(1, numberToCheck + 1):
    if number % 3 == 0:
        amountOfMultiples += 1

print("That number has " + str(amountOfMultiples) + " multiples of 3!")
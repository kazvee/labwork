numberToCheck = int(input("Enter a number to check if it is prime: "))

if numberToCheck <= 1:
    print(numberToCheck, "is not a prime number!")
else:
    for number in range(2, int(numberToCheck**0.5) + 1):
        if numberToCheck % number == 0:
            print(numberToCheck, "is not a prime number!")
            break
    else:
        print(numberToCheck, "is a prime number!")
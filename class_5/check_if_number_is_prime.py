number_to_check = int(input("Enter a number to check if it is prime: "))

if number_to_check <= 1:
    print(number_to_check, "is not a prime number!")
else:
    for number in range(2, int(number_to_check**0.5) + 1):
        if number_to_check % number == 0:
            print(number_to_check, "is not a prime number!")
            break
    else:
        print(number_to_check, "is a prime number!")
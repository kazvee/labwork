number_to_check = int(input("Enter a number to check how many multiples of 3 there are: "))

amount_of_multiples = 0

for number in range(1, number_to_check + 1):
    if number % 3 == 0:
        amount_of_multiples += 1

print("That number has " + str(amount_of_multiples) + " multiples of 3!")
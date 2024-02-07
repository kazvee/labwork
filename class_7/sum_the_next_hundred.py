starting_number = int(input("Enter a number: "))

sum = 0
for number in range(starting_number, starting_number + 101):
    sum += number

print(sum)
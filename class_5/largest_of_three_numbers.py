first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

if first > second and first > third:
    largest_number = first
elif second > third:
    largest_number = second
else:
    largest_number = third

print("The largest number is: ", largest_number)
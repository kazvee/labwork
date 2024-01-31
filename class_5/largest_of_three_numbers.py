first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

if first > second and first > third:
    largestNumber = first
elif second > third:
    largestNumber = second
else:
    largestNumber = third

print("The largest number is: ", largestNumber)
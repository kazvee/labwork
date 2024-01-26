first = int(input("Enter the first number: "))
second = int(input("Enter the second number:"))

if first > second:
    print("The larger number is:")
    print(first)
elif first < second:
    print("The larger number is:")
    print(second)
else: 
    print("The numbers are equal.")
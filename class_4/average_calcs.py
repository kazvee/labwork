try:
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))
    
    result = (first + second) / 2
    print("The average of those two numbers is:", result)

except ValueError:
    print("Error: Please enter two numbers")
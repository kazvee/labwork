try:
    first = int(input("Enter the first temperature: "))
    second = int(input("Enter the second temperature: "))
    third = int(input("Enter the third temperature: "))
    
    sum = (first + second + third)
    average = sum / 3

    print("The sum of all temperature is: ", sum)
    print("The average of temperature is: ", average)

except ValueError:
    print("Error: Please enter three numbers")
def is_leap_year(year):
    if (year % 4 != 0):
        return False
    elif (year % 100 != 0):
        return True
    elif (year % 400 != 0):
        return False
    else:
        return True

while True:
    user_input = input("Enter a year: ")
    if user_input.isdigit():
        year_to_check = int(user_input)
        break
    
result = is_leap_year(year_to_check)

if result:
    print(year_to_check, "is a leap year! 🐰")
else:
    print(year_to_check, "is not a leap year. 🐶")
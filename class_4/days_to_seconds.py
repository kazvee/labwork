days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

result = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds

print("Total seconds is:")
print(result)
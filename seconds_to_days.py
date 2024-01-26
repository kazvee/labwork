total_seconds = int(input("Enter the number of seconds: "))

days = total_seconds // (24 * 60 * 60)
leftover_seconds_from_days = total_seconds % (24 * 60 * 60)

hours = leftover_seconds_from_days // (60 * 60)
leftover_seconds_after_hours = leftover_seconds_from_days % (60 * 60)

minutes = leftover_seconds_after_hours // 60
seconds = leftover_seconds_after_hours % 60

print("Days: ")
print(days)
print("Hours: ")
print(hours)
print("Minutes: ")
print(minutes)
print("Seconds: ") 
print(seconds)
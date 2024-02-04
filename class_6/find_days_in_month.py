import calendar

def days_in_month(year, month):
    if 1 <= month <= 12:
        return calendar.monthrange(year, month)[1]
    else:
        return 0

year = int(input("🤔 Enter the year: "))
month = int(input("🤔 Enter the month (1 to 12): "))

result = days_in_month(year, month)

if result == 0:
    print("🙈 Invalid month. Please enter a value between 1 and 12.")
else:
    print("📅 There are", result, "days in", calendar.month_name[month], year, end="!\n")
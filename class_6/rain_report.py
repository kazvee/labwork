import calendar

def days_in_month(year, month):
    if 1 <= month <= 12:
        return calendar.monthrange(year, month)[1]
    else:
        return 0

def collect_rain_data():
    year = int(input("📅 Enter the year: "))
    month = int(input("📆 Enter the month (1 to 12): "))

    days_in_month_value = days_in_month(year, month)

    if days_in_month_value > 0:
        total_precipitation = 0
        max_precipitation = 0
        max_precipitation_days = []
        consecutive_rain_days = 0
        previous_day_rain = False

        for day in range(1, days_in_month_value + 1):
            while True:
                try:
                    precipitation = float(input(f"☔ Enter precipitation for {year}-{month:02d}-{day:02d} (mm): "))
                    if precipitation < 0:
                        print("🙈 Please enter a non-negative value for precipitation.")
                        continue
                    break
                except ValueError:
                    print("🙈 Please enter a valid numeric value.")

            total_precipitation += precipitation

            if precipitation > max_precipitation:
                max_precipitation = precipitation
                max_precipitation_days = [day]
            elif precipitation == max_precipitation:
                max_precipitation_days.append(day)

            if precipitation > 0:
                if not previous_day_rain:
                    consecutive_rain_days += 1
                previous_day_rain = True
            else:
                previous_day_rain = False

        print("\n📊 Total precipitation for the month:", total_precipitation, "mm")
        print("🌧️ Maximum precipitation in a day:", max_precipitation, "mm on day(s)", ', '.join(map(str, max_precipitation_days)))

        if consecutive_rain_days >= 2:
            print("🌧️ It rained two or more days in a row.")
        else:
            print("🌦️ It did not rain two days in a row.")

    else:
        print("🙈 Invalid month. Please enter a value between 1 and 12.")

collect_rain_data()
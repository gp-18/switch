# Display a calendar for a given month and year using a dictionary
import calendar

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

if month in months:
    print(f"\n{months[month]} {year}")
    print(calendar.month(year, month))
else:
    print("Invalid month. Please enter a number between 1 and 12.")
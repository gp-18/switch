# Take a month number (1–12) and print the number of days in that month (ignore leap years).
# Example 1: Input: 2024 -> Output: Leap year
# Example 2: Input: 2023 -> Output: Not a leap year

number = int(input("Enter the month number (1-12): "))

if number in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days in month")
elif number in [4, 6, 9, 11]:
    print("30 days in month")
elif number == 2:
    print("28 days in month")
else:
    print("Invalid month number")

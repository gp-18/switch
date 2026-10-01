# Check whether a year is a leap year.

# Example 1:
# Input: 2024
# Output: 2024 is a leap year

# Example 2:
# Input: 1900
# Output: 1900 is not a leap year (divisible by 100 but not 400)

year = int(input("Enter a year: "))

# A year is a leap year if divisible by 4 AND (not divisible by 100 OR divisible by 400)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

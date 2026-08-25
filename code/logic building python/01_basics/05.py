# Check if a given year is a leap year.
# Example 1: Input: 2024 -> Output: Leap year
# Example 2: Input: 2023 -> Output: Not a leap year

number = int(input("give the year : "))

if number % 4 == 0 and not number % 100 == 0  or number % 400 == 0 : 
    print("yes its a leap year")
else : 
    print("no its not a leap year")

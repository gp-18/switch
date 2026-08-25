# Take a year and print the corresponding century (e.g., '19th century', '20th century').
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

year = int(input("Enter the year: "))

if year > 0:
    century = (year - 1) // 100 + 1
    print(f"{century}th century")
else:
    print("Invalid year")

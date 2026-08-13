# Take a year and print the corresponding century (e.g., '19th century', '20th century').
year = int(input("Enter the year: "))

if year > 0:
    century = (year - 1) // 100 + 1
    print(f"{century}th century")
else:
    print("Invalid year")
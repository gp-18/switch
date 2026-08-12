# Check if a given year is a leap year.

number = int(input("give the year : "))

if number % 4 == 0 and not number % 100 == 0  or number % 400 == 0 : 
    print("yes its a leap year")
else : 
    print("no its not a leap year")
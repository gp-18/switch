# Take a weekday number (1–7) and determine if it is a weekday or weekend.

number = int(input("enter the number : "))


print("weekdays") if number in range(1,6) else print("weekend")
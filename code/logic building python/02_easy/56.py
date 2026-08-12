# Check if one of two given numbers is a multiple of the other.

number1 = int(input("Enter the number 1: "))
number2 = int(input("Enter the number 2: "))

if number2 % number1 == 0 or number1 % number2 == 0:
    print("One number is a multiple of the other")
else:
    print("Neither number is a multiple of the other")
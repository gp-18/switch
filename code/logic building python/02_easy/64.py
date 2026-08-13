# Check if a number is a multiple of 7 or ends with 7.

number = int(input("Enter the number : "))
last_digit = number % 10 

if number % 7 == 0 or last_digit == 7 : 
    print("yes the number is multiple of 7 or its end with the 7")
    
# Take three numbers and print the largest.

number1 = float(input("Enter the number 1 : "))
number2 = float(input("Enter the number 2 : "))
number3 = float(input("Enter the number 3 : "))


print(f"{number1} is the greatest") if  number1 > number2 and number1 > number3 else print(f"{number2} is the greatest")if number2 > number1 and number2 > number3 else print(f"{number3} is the greatest")
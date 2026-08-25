# Take three numbers and print the largest.
# Example 1: Input: 10, 20 -> Output: 20
# Example 2: Input: 5, 3, 9 -> Output: 9

number1 = float(input("Enter the number 1 : "))
number2 = float(input("Enter the number 2 : "))
number3 = float(input("Enter the number 3 : "))


print(f"{number1} is the greatest") if  number1 > number2 and number1 > number3 else print(f"{number2} is the greatest")if number2 > number1 and number2 > number3 else print(f"{number3} is the greatest")

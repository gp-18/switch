# Take two numbers and print the larger one.
# Example 1: Input: 10, 20 -> Output: 20
# Example 2: Input: 5, 3, 9 -> Output: 9

number1 = float(input("enter the number 1 : "))
number2 = float(input("enter the number 2 : "))


print(f"{number1} is greater ") if number1 > number2 else print(f"{number2} is greater")

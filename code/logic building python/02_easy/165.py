# Simulate a simple calculator using if-elif (supporting +, -, *, /).
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

number1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
number2 = float(input("Enter the second number: "))

if operator == "+":
    result = number1 + number2
    print("Result:", result)

elif operator == "-":
    result = number1 - number2
    print("Result:", result)

elif operator == "*":
    result = number1 * number2
    print("Result:", result)

elif operator == "/":

    if number2 == 0:
        print("Cannot divide by zero")
    else:
        result = number1 / number2
        print("Result:", result)

else:
    print("Invalid operator")

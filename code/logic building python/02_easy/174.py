# Build a simple calculator with 4 basic operations (+, -, *, /).
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

number1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
number2 = float(input("Enter the second number: "))

if operator == "+":
    print("Result:", number1 + number2)

elif operator == "-":
    print("Result:", number1 - number2)

elif operator == "*":
    print("Result:", number1 * number2)

elif operator == "/":

    if number2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", number1 / number2)

else:
    print("Invalid operator")

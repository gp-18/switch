# Swap two variables using a temporary variable.
number1 = int(input("Enter the number 1 : "))
number2 = int(input("Enter the number 2 : "))

number1 , number2 = number2 , number1

print(f"{number1} is and {number2} is")
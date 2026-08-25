# Swap two variables using a temporary variable.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

number1 = int(input("Enter the number 1 : "))
number2 = int(input("Enter the number 2 : "))

number1 , number2 = number2 , number1

print(f"{number1} is and {number2} is")

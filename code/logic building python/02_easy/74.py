# Take two numbers and check if both are positive and their sum is less than 100.
# Example 1: Input: 5 -> Output: 15
# Example 2: Input: 10 -> Output: 55

if (number1 := int(input("Enter the number 1: "))) > 0 and (number2 := int(input("Enter the number 2: "))) > 0:
    print("Yes") if number1 + number2 < 100 else print("No")
else:
    print("Invalid input")

# Check if one of two given numbers is a multiple of the other.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

number1 = int(input("Enter the number 1: "))
number2 = int(input("Enter the number 2: "))

if number2 % number1 == 0 or number1 % number2 == 0:
    print("One number is a multiple of the other")
else:
    print("Neither number is a multiple of the other")

# Take three numbers and print the median value (neither maximum nor minimum).
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))

if (number1 >= number2 and number1 <= number3) or (number1 <= number2 and number1 >= number3):
    print("Median:", number1)

elif (number2 >= number1 and number2 <= number3) or (number2 <= number1 and number2 >= number3):
    print("Median:", number2)

else:
    print("Median:", number3)

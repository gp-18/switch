# Find the LCM of two numbers.
# Example 1: Input: 4, 6 -> Output: 12
# Example 2: Input: 5, 10 -> Output: 10

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > 0 and number2 > 0:

    if number1 > number2:
        lcm = number1
    else:
        lcm = number2

    while True:

        if lcm % number1 == 0 and lcm % number2 == 0:
            break

        lcm += 1

    print("LCM:", lcm)

else:
    print("Enter positive numbers")

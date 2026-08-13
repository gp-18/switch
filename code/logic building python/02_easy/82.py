# Find the sum of digits of a number.

if (number := int(input("Enter the number: "))) != 0:
    digit_sum = 0

    while number > 0:
        last_digit = number % 10
        digit_sum = digit_sum + last_digit
        number = number // 10

    print(digit_sum)
else:
    print("Enter the valid number")
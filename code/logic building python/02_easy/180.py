# Check if a number is a Harshad (Niven) number.
# Example 1: Input: 18 -> Output: Harshad number
# Example 2: Input: 19 -> Output: Not a Harshad number

number = int(input("Enter the number: "))

if number > 0:
    temp = number
    digit_sum = 0

    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    if number % digit_sum == 0:
        print("Harshad number")
    else:
        print("Not a Harshad number")
else:
    print("Please enter a positive integer")

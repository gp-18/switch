# Check whether a given integer is single-digit, double-digit, or multi-digit.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

number = int(input("Enter an integer: "))

if -9 <= number <= 9:
    print("Single-digit")
elif -99 <= number <= 99:
    print("Double-digit")
else:
    print("Multi-digit")

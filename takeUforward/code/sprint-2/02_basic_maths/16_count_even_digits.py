# Count Even Digits
# Count how many digits in an integer n are even.
#
# Example 1:
# Input: n = 123456
# Output: 3  # Digits: 2, 4, 6
#
# Example 2:
# Input: n = 13579
# Output: 0
#
# Example 3 (Edge Case - Negative Number with Zeros):
# Input: n = -2048
# Output: 4  # Digits 2, 0, 4, 8 are all even

number = abs(int(input("Enter the number : ")))

if number == 0:
    print(1)
else:
    even_count = 0

    while number > 0:
        last_digit = number % 10

        if last_digit % 2 == 0:
            even_count += 1

        number = number // 10

    print(even_count)
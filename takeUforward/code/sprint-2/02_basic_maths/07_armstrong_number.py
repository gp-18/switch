# Armstrong Number
# Check whether a number is an Armstrong number (the sum of each digit raised to the power of the total number of digits equals the number).
#
# Example 1:
# Input: n = 153
# Output: True  # 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
#
# Example 2:
# Input: n = 123
# Output: False
#
# Example 3 (Edge Case - Single Digit):
# Input: n = 7
# Output: True  # 7^1 = 7

number = input("Enter the number : ")

length_of_number = len(number)
copy_of_number = int(number)
number = int(number)

ans = 0

while number > 0:
    last_digit = number % 10
    ans = ans + pow(last_digit, length_of_number)
    number = number // 10

print("yes") if ans == copy_of_number else print("no")

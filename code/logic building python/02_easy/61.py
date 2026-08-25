# Take a 3-digit number and check if all digits are distinct.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

number = int(input("Enter the 3 digit number: "))
set_value = set()

while number != 0:
    last_digit = number % 10
    set_value.add(last_digit)
    number = number // 10

if len(set_value) == 3:
    print("All digits are distinct")
else:
    print("Digits are not distinct")

# Square every digit of a number and return as an integer.
# Example 1: Input: 9119 -> Output: 811181 (9^2=81, 1^2=1, 1^2=1, 9^2=81)
# Example 2: Input: 2489 -> Output: 4166481

num_str = input("Enter a number: ")

squared_digits = "".join(str(int(digit) ** 2) for digit in num_str if digit.isdigit())
print("Resulting integer:", int(squared_digits))

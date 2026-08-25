# Check if a number lies within the range [100, 999].
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

number = int(input("enter the number to check the range : "))


print(f"yes in range {number}") if 100 <= number  <= 999 else print(f"not in range {number}")

# Find the nth triangular number.
# Example 1: Input: 5 -> Output: 15
# Example 2: Input: 6 -> Output: 21

n = int(input("Enter n: "))

if n >= 1:
    triangular_num = n * (n + 1) // 2
    print(f"{n}th triangular number is:", triangular_num)
else:
    print("Please enter a positive integer")

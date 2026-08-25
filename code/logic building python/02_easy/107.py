# Find nth Fibonacci number recursively.
# Example 1: Input: 5 -> Output: 5
# Example 2: Input: 6 -> Output: 8

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter n: "))
if n >= 0:
    print(f"{n}th Fibonacci number:", fibonacci(n))
else:
    print("Please enter a non-negative integer")

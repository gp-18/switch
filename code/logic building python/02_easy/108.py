# Print Fibonacci series up to n terms recursively.
# Example 1: Input: 5 -> Output: 0 1 1 2 3
# Example 2: Input: 3 -> Output: 0 1 1

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n_terms = int(input("Enter number of terms: "))
if n_terms >= 1:
    series = [fibonacci(i) for i in range(n_terms)]
    print("Fibonacci series:", *series)
else:
    print("Please enter a positive integer")

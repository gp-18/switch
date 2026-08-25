# Find all even numbers from 1 to n using list comprehension.
# Example 1: Input: 10 -> Output: [2, 4, 6, 8, 10]
# Example 2: Input: 7 -> Output: [2, 4, 6]

n = int(input("Enter n: "))

evens = [i for i in range(1, n + 1) if i % 2 == 0]
print("Even numbers:", evens)

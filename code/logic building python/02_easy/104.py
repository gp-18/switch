# Find sum of first n natural numbers recursively.
# Example 1: Input: 5 -> Output: 15
# Example 2: Input: 10 -> Output: 55

def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 1)

number = int(input("Enter the number n: "))
if number >= 1:
    print("Sum:", recursive_sum(number))
else:
    print("Please enter a positive integer")

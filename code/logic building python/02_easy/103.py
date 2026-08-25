# Print only odd numbers from 1 to n recursively.
# Example 1: Input: 10 -> Output: 1 3 5 7 9
# Example 2: Input: 5 -> Output: 1 3 5

def print_odd(n, current=1):
    if current > n:
        return
    print(current, end=" ")
    print_odd(n, current + 2)

number = int(input("Enter the number n: "))
if number >= 1:
    print_odd(number)
    print()
else:
    print("Please enter a positive integer")

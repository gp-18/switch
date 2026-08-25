# Print only even numbers from 1 to n recursively.
# Example 1: Input: 10 -> Output: 2 4 6 8 10
# Example 2: Input: 5 -> Output: 2 4

def print_even(n, current=2):
    if current > n:
        return
    print(current, end=" ")
    print_even(n, current + 2)

number = int(input("Enter the number n: "))
if number >= 2:
    print_even(number)
    print()
else:
    print("No even numbers in range")

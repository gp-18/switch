# Print numbers from 1 to n using recursion.
# Example 1: Input: 5 -> Output: 1 2 3 4 5
# Example 2: Input: 3 -> Output: 1 2 3

def print_1_to_n(n, current=1):
    if current > n:
        return
    print(current, end=" ")
    print_1_to_n(n, current + 1)

number = int(input("Enter the number n: "))
if number >= 1:
    print_1_to_n(number)
    print()
else:
    print("Please enter a positive integer")

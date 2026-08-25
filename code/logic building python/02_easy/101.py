# Print numbers from n down to 1 using recursion.
# Example 1: Input: 5 -> Output: 5 4 3 2 1
# Example 2: Input: 3 -> Output: 3 2 1

def print_n_to_1(n):
    if n < 1:
        return
    print(n, end=" ")
    print_n_to_1(n - 1)

number = int(input("Enter the number n: "))
if number >= 1:
    print_n_to_1(number)
    print()
else:
    print("Please enter a positive integer")

# Find the cube sum of first n natural numbers.
# Example 1: Input: 5 -> Output: Cube sum of first 5 natural numbers is: 225
# Example 2: Input: 3 -> Output: Cube sum of first 3 natural numbers is: 36

n = int(input("Enter the number n: "))

if n >= 1:
    # Formula approach: (n * (n + 1) // 2) ** 2
    cube_sum = (n * (n + 1) // 2) ** 2
    print(f"Cube sum of first {n} natural numbers is: {cube_sum}")
else:
    print("Please enter a valid positive integer")

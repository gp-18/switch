# Print all numbers between a and b divisible by 7.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))

for i in range(a, b + 1):
    if i % 7 == 0:
        print(i)

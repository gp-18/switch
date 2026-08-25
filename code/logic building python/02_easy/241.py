# Return how many of three integers are equal (0, 2, or 3).
# Example 1: Input: 3, 4, 3 -> Output: 2
# Example 2: Input: 1, 1, 1 -> Output: 3

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

unique_count = len({a, b, c})
if unique_count == 1:
    print("Equal numbers: 3")
elif unique_count == 2:
    print("Equal numbers: 2")
else:
    print("Equal numbers: 0")

# Take three sides and check if they form a valid triangle.
# Example 1: Input: 3, 4, 5 -> Output: Valid triangle
# Example 2: Input: 1, 2, 10 -> Output: Invalid triangle

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")

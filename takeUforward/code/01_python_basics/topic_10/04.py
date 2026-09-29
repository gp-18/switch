# Print a multiplication table for a number supplied by the user.

# Example 1:
# Input: 3
# Output:
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30

# Example 2:
# Input: 5
# Output:
# 5 x 1 = 5
# ...
# 5 x 10 = 50

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

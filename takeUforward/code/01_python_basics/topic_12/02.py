# Print a right-angled triangle of stars with n rows.

# Example 1:
# Input: n = 3
# Output:
# *
# * *
# * * *

# Example 2:
# Input: n = 4
# Output:
# *
# * *
# * * *
# * * * *

n = int(input("Enter number of rows (n): "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

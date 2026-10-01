# Print a multiplication grid from 1 to 5.

# Example 1:
# Output (rows 1 to 3):
# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15

# Example 2:
# Output (row 5): 5 10 15 20 25

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2d}", end=" ")
    print()

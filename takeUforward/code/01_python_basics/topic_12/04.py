# Print all ordered pairs (i, j) where both values range from 1 to 3.

# Example 1:
# Output (pairs with i = 1): (1, 1), (1, 2), (1, 3)

# Example 2:
# Output (total 9 pairs): (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)

for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()

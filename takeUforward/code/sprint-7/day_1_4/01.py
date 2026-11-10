# Search in 2D Matrix - II
# Given a 2D matrix where each row is sorted in ascending order from left to right,
# and each column is sorted in ascending order from top to bottom.
# Determine if an integer target exists in the matrix.
#
# Example 1:
# Input:  matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], target = 5
# Output: True
# Explanation: Target 5 exists at index (1, 1).
#
# Example 2:
# Input:  matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], target = 20
# Output: False
#
# Example 3:
# Input:  matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], target = 1
# Output: True
#
# Think About:
# - Virtual 1D flattening fails because row transitions are not strictly sorted.
# - Start at top-right corner (0, m - 1): moving left decreases, moving down increases.
# - If matrix[row][col] == target: return True.
# - If matrix[row][col] < target: eliminate current row (row += 1).
# - If matrix[row][col] > target: eliminate current column (col -= 1).
# - Time Complexity: O(n + m)
# - Space Complexity: O(1) auxiliary space
#

rows = int(input("Enter number of rows (n) : "))
cols = int(input("Enter number of columns (m) : "))
matrix = []

for r in range(rows):
    current_row = []
    for c in range(cols):
        val = int(input(f"Enter element at [{r}][{c}] : "))
        current_row.append(val)
    matrix.append(current_row)

target = int(input("Enter target value : "))

print(f"Your matrix ({rows}x{cols}) : {matrix} with target = {target}")

# Write your solution below:
# Optimal Approach: Top-Right Corner Staircase Elimination
# Time Complexity: O(n + m) | Space Complexity: O(1)

def search_matrix_ii(mat, target_val):
    n = len(mat)
    m = len(mat[0])

    # Start at top-right corner
    row = 0
    col = m - 1

    while row < n and col >= 0:
        if mat[row][col] == target_val:
            return True
        elif mat[row][col] < target_val:
            # All elements left in this row are smaller -> eliminate row
            row += 1
        else:
            # All elements below in this column are larger -> eliminate column
            col -= 1

    return False

ans = search_matrix_ii(matrix, target)

print(f"Target {target} found in matrix : {ans}")

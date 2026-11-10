# Find Row with Maximum 1's
# Given a non-empty binary grid mat of size n x m consisting of 0s and 1s,
# where every row is sorted in ascending order.
# Find the 0-based index of the row with the maximum number of 1s.
# If two rows tie, return the smaller row index. If no 1 exists, return -1.
#
# Example 1:
# Input:  mat = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
# Output: 0
# Explanation: Row 0 has 3 ones, which is the maximum.
#
# Example 2:
# Input:  mat = [[0, 0], [0, 0]]
# Output: -1
# Explanation: Matrix contains no 1s.
#
# Example 3:
# Input:  mat = [[0, 0, 1], [0, 1, 1], [0, 1, 1]]
# Output: 1
# Explanation: Rows 1 and 2 both have 2 ones; smaller index is 1.
#
# Think About:
# - Binary search per row finds the first 1 (lower_bound) in O(n * log m).
# - Optimal O(n + m): Start at top-right corner (row = 0, col = m - 1).
# - If mat[row][col] == 1: current row beats previous records -> ans = row, move left (col -= 1).
# - Else (mat[row][col] == 0): row is sorted so nothing left can be 1 -> move down (row += 1).
# - Time Complexity: O(n + m)
# - Space Complexity: O(1) auxiliary space
#

rows = int(input("Enter number of rows (n) : "))
cols = int(input("Enter number of columns (m) : "))
matrix = []

for r in range(rows):
    current_row = []
    for c in range(cols):
        val = int(input(f"Enter element at [{r}][{c}] (0 or 1) : "))
        current_row.append(val)
    matrix.append(current_row)

print(f"Your matrix ({rows}x{cols}) : {matrix}")

# Write your solution below:
# Optimal Approach: Top-Right Staircase Traversal
# Time Complexity: O(n + m) | Space Complexity: O(1)

def row_with_max_1s(mat):
    n = len(mat)
    m = len(mat[0])

    # Start at top-right corner
    row = 0
    col = m - 1
    ans = -1

    while row < n and col >= 0:
        if mat[row][col] == 1:
            # This row has strictly more 1s than previous rows checked
            ans = row
            col -= 1
        else:
            # All elements to the left are 0; skip down to the next row
            row += 1

    return ans

ans = row_with_max_1s(matrix)

print(f"The row with maximum number of 1's is : {ans}")

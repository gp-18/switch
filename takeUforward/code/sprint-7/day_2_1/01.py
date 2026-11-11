# Find Peak Element - II
# Given a 0-indexed n x m matrix mat where no two adjacent cells are equal,
# find any peak element mat[i][j] and return [i, j].
# A peak element is strictly greater than its left, right, top, and bottom neighbors.
# Outer perimeter cells are assumed to be -1.
#
# Example 1:
# Input:  mat = [[10, 20, 15], [21, 30, 14], [7, 16, 32]]
# Output: [1, 1] (or [2, 2])
#
# Example 2:
# Input:  mat = [[10, 7], [11, 17]]
# Output: [1, 1]
#
# Example 3:
# Input:  mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [2, 2]
#
# Think About:
# - Binary search over columns [0, m - 1].
# - For mid column, find the row index containing the global max in column mid.
# - Since it's the column max, it automatically beats top and bottom neighbors!
# - Compare against left (mid - 1) and right (mid + 1) neighbors:
#   * If greater than both: peak found, return [row, mid].
#   * If left > mat[row][mid]: peak guaranteed on left -> high = mid - 1.
#   * Else: peak guaranteed on right -> low = mid + 1.
# - Time Complexity: O(n * log m)
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

print(f"Your matrix ({rows}x{cols}) : {matrix}")

# Write your solution below:
# Optimal Approach: Binary Search on Columns [0, m - 1]
# Time Complexity: O(n * log m) | Space Complexity: O(1)

def max_element_row(mat, col):
    n = len(mat)
    max_val = float('-inf')
    index = -1

    for i in range(n):
        if mat[i][col] > max_val:
            max_val = mat[i][col]
            index = i

    return index

def find_peak_grid(mat):
    m = len(mat[0])
    low = 0
    high = m - 1

    while low <= high:
        mid = low + (high - low) // 2

        # Row index of the maximum element in column mid
        row = max_element_row(mat, mid)

        left = mat[row][mid - 1] if mid - 1 >= 0 else -1
        right = mat[row][mid + 1] if mid + 1 < m else -1

        if mat[row][mid] > left and mat[row][mid] > right:
            return [row, mid]
        elif left > mat[row][mid]:
            # Larger element to the left guarantees a peak in the left half
            high = mid - 1
        else:
            # Larger element to the right guarantees a peak in the right half
            low = mid + 1

    return [-1, -1]

ans = find_peak_grid(matrix)

print(f"A peak element is at coordinates : {ans}")

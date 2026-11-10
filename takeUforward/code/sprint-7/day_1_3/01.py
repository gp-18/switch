# Search in a 2D Matrix
# Given a 2D array mat where each row is sorted in non-decreasing order,
# and the first element of a row is greater than the last element of the previous row.
# Determine if an integer target exists in the given mat or not.
#
# Example 1:
# Input:  mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], target = 8
# Output: True
# Explanation: Target 8 exists at index (1, 3).
#
# Example 2:
# Input:  mat = [[1, 2, 4], [6, 7, 8], [9, 10, 34]], target = 78
# Output: False
#
# Example 3:
# Input:  mat = [[1, 2, 4], [6, 7, 8], [9, 10, 34]], target = 7
# Output: True
#
# Think About:
# - Virtual 1D flattening: treat matrix as sorted 1D array of length n * m.
# - Search range: low = 0, high = n * m - 1.
# - Map 1D index mid to 2D coordinates in O(1): row = mid // m, col = mid % m.
# - Compare mat[row][col] with target and eliminate half the search space.
# - Time Complexity: O(log(n * m))
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
# Optimal Approach: Virtual 1D Binary Search
# Time Complexity: O(log(n * m)) | Space Complexity: O(1)

def search_matrix(mat, target_val):
    n = len(mat)
    m = len(mat[0])

    low = 0
    high = n * m - 1

    while low <= high:
        mid = low + (high - low) // 2

        # Convert 1D index to 2D matrix coordinates
        row = mid // m
        col = mid % m

        if mat[row][col] == target_val:
            return True
        elif mat[row][col] < target_val:
            low = mid + 1
        else:
            high = mid - 1

    return False

ans = search_matrix(matrix, target)

print(f"Target {target} found in matrix : {ans}")

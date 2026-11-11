# Matrix Median
# Given a 2D array matrix that is row-wise sorted (where N * M is odd).
# Find and return the median of the given matrix.
#
# Example 1:
# Input:  matrix = [[1, 4, 9], [2, 5, 6], [3, 7, 8]]
# Output: 5
# Explanation: Flattened sorted elements: [1, 2, 3, 4, 5, 6, 7, 8, 9]. Median = 5.
#
# Example 2:
# Input:  matrix = [[1, 3, 8], [2, 3, 4], [1, 2, 5]]
# Output: 3
# Explanation: Flattened sorted elements: [1, 1, 2, 2, 3, 3, 4, 5, 8]. Median = 3.
#
# Example 3:
# Input:  matrix = [[1, 4, 15], [2, 5, 6], [3, 8, 11]]
# Output: 5
#
# Think About:
# - Search space on values: low = min of first column, high = max of last column.
# - Median is the smallest value X where count of matrix elements <= X is > (n * m) // 2.
# - Use upper_bound (first index > X) in each sorted row to count elements <= X in O(log m).
# - If small_equal <= req: mid is too small -> low = mid + 1.
# - Else: search left for smallest valid value -> high = mid - 1.
# - Time Complexity: O(n * log m * log(max - min + 1))
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
# Optimal Approach: Binary Search on Value Space + Upper Bound per Row
# Time Complexity: O(n * log m * log(max - min + 1)) | Space Complexity: O(1)

def upper_bound(arr, x, m):
    low = 0
    high = m - 1
    ans = m

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > x:
            ans = mid
            # Search left for an earlier element strictly greater than x
            high = mid - 1
        else:
            low = mid + 1

    return ans

def count_small_equal(mat, n, m, x):
    cnt = 0
    for i in range(n):
        cnt += upper_bound(mat[i], x, m)
    return cnt

def find_median(mat):
    n = len(mat)
    m = len(mat[0])

    low = float('inf')
    high = float('-inf')

    for i in range(n):
        low = min(low, mat[i][0])
        high = max(high, mat[i][m - 1])

    req = (n * m) // 2

    while low <= high:
        mid = low + (high - low) // 2
        small_equal = count_small_equal(mat, n, m, mid)

        if small_equal <= req:
            # Too few elements <= mid, search higher values
            low = mid + 1
        else:
            # Enough elements <= mid, search for smaller value
            high = mid - 1

    return low

ans = find_median(matrix)

print(f"The median of the matrix is : {ans}")

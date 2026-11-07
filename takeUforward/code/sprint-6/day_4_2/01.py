# Kth Missing Positive Number
# Given a sorted array of unique positive integers arr,
# return the kth missing positive number that is not present in arr.
#
# Example 1:
# Input:  arr = [3, 5, 7, 10], k = 6
# Output: 9
# Explanation: Missing numbers: [1, 2, 4, 6, 8, 9, 11, ...]. 6th missing is 9.
#
# Example 2:
# Input:  arr = [1, 4, 6, 8, 9], k = 3
# Output: 5
# Explanation: Missing numbers: [2, 3, 5, 7, 10, ...]. 3rd missing is 5.
#
# Example 3:
# Input:  arr = [2, 3, 7, 11, 15], k = 5
# Output: 8
#
# Think About:
# - In a complete sequence without missing numbers, arr[i] == i + 1.
# - Number of missing integers before index i: missing = arr[i] - (i + 1).
# - If missing < k: the kth missing number lies to the right (left = mid + 1).
# - Else: search left (right = mid - 1).
# - At termination, left points to the index where the kth missing number falls.
# - Formula: ans = left + k.
# - Time Complexity: O(log N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter element at index {i} : "))
    array.append(value)

k = int(input("Enter k : "))

print(f"Your sorted array : {array} with k = {k}")

# Write your solution below:
# Optimal Approach: Binary Search on Indices [0, n - 1]
# Time Complexity: O(log N) | Space Complexity: O(1)

left = 0
right = length - 1

while left <= right:
    mid = left + (right - left) // 2

    # Calculate missing numbers before index mid
    missing = array[mid] - (mid + 1)

    if missing < k:
        # Need more missing numbers, search in right half
        left = mid + 1
    else:
        # At least k missing numbers reached, search in left half
        right = mid - 1

# Mathematical derivation: ans = array[right] + (k - missing_at_right) = left + k
ans = left + k

print(f"The {k}th missing positive number is : {ans}")


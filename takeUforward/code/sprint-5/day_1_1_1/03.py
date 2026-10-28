# Majority Element in a Sorted Array
# Given a sorted array nums of size n, determine if there exists an element that
# appears more than n / 2 times. If so, return that element; otherwise return -1.
#
# Example 1:
# Input:  nums = [2, 4, 5, 5, 5, 5, 5, 6, 6]
# Output: 5
#
# Example 2:
# Input:  nums = [10, 20, 30, 40]
# Output: -1
#
# Think About:
# - In a sorted array, the candidate must be at index n // 2.
# - Verify frequency via binary search or linear check.
# - Time Complexity: O(log N) or O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your sorted array has become : {array} and now doing the operations on it.")

# Write your solution below:

from bisect import bisect_left

# Optimal Approach (Exploiting Sorted Order with Binary Search)
# Time Complexity: O(log N) | Space Complexity: O(1)

if length == 0:
    print("Majority element is: -1")
else:
    # 1. In a sorted array, any majority element MUST occupy the middle index
    candidate = array[length // 2]

    # 2. Find the first occurrence index of the candidate using binary search
    first_idx = bisect_left(array, candidate)

    # 3. Check if candidate spans more than length // 2 positions
    if first_idx + length // 2 < length and array[first_idx + length // 2] == candidate:
        print(f"Majority element is: {candidate}")
    else:
        print("Majority element is: -1")


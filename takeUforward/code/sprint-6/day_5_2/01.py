# Find Peak Element
# Given an array arr of integers, find the index of a peak element.
# An element is a peak if it is strictly greater than its neighbors.
# For boundaries, elements outside the array are considered -infinity.
# If multiple peaks exist, return the index of any peak.
#
# Example 1:
# Input:  arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
# Output: 7
# Explanation: At index 7 (value 8), 7 < 8 and 8 > 5. Peak index is 7.
#
# Example 2:
# Input:  arr = [1, 2, 1, 3, 5, 6, 4]
# Output: 1 (or 5)
# Explanation: Both index 1 and index 5 are peaks.
#
# Example 3:
# Input:  arr = [-2, -1, 3, 4, 5]
# Output: 4
#
# Think About:
# - Handle boundaries first: index 0 (check arr[0] > arr[1]) and index n-1 (check arr[n-1] > arr[n-2]).
# - Search interior range: low = 1, high = n - 2.
# - If arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]: mid is a peak!
# - If arr[mid] > arr[mid - 1]: on an upward slope, peak must exist on right (low = mid + 1).
# - Else: on a downward slope/valley, peak must exist on left (high = mid - 1).
# - Time Complexity: O(log N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter element at index {i} : "))
    array.append(value)

print(f"Your array : {array}")

# Write your solution below:
# Optimal Approach: Binary Search on Index Range [1, n - 2]
# Time Complexity: O(log N) | Space Complexity: O(1)

def find_peak_element(arr):
    n = len(arr)

    # Edge cases: 1 element, or boundaries are peaks
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    # Search in interior indices [1, n - 2]
    low = 1
    high = n - 2

    while low <= high:
        mid = low + (high - low) // 2

        # Check if mid is a peak
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        # Upward slope: a peak must lie on the right
        if arr[mid] > arr[mid - 1]:
            low = mid + 1
        # Downward slope or valley: a peak must lie on the left
        else:
            high = mid - 1

    return -1

ans = find_peak_element(array)

print(f"A peak element is at index : {ans}")


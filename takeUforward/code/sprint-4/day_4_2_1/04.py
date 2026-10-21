# Three-Way Partitioning Around a Range [lowVal, highVal] (Amazon, Microsoft, Adobe)
# Given an array nums and a range [lowVal, highVal], rearrange the elements in-place such that:
#   1. All elements strictly smaller than lowVal appear first.
#   2. All elements in the range [lowVal, highVal] (inclusive) appear next.
#   3. All elements strictly greater than highVal appear last.
#
# Example 1:
# Input:  nums = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32], lowVal = 10, highVal = 20
# Output: [1, 5, 4, 2, 1, 3, 14, 20, 20, 98, 87, 32, 54]
#
# Example 2:
# Input:  nums = [1, 2, 3, 3, 4], lowVal = 1, highVal = 2
# Output: [1, 2, 3, 3, 4]
#
# Example 3 (Edge Case):
# Input:  nums = [5, 5, 5], lowVal = 10, highVal = 20
# Output: [5, 5, 5]  # All elements smaller than lowVal
#
# Think About:
# - Dutch National Flag with Range boundaries:
#   * low = 0, mid = 0, high = n - 1
#   * While mid <= high:
#       - If nums[mid] < lowVal: swap nums[low] and nums[mid], low += 1, mid += 1
#       - Else if nums[mid] > highVal: swap nums[mid] and nums[high], high -= 1 (do NOT increment mid)
#       - Else (lowVal <= nums[mid] <= highVal): mid += 1
# - Time Complexity: O(N)
# - Space Complexity: O(1) in-place
#

length = int(input("Enter the length of the array: "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i}: "))
    array.append(value)

lowVal = int(input("Enter lowVal: "))
highVal = int(input("Enter highVal: "))

print(f"Your array has become: {array}, range is: [{lowVal}, {highVal}] and now doing the operations on it.")

# Write your solution below

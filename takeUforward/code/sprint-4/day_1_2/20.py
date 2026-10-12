# Valid Mountain Array
# Given an array of integers arr, return True if and only if it is a valid mountain array.
# An array is a mountain array if len(arr) >= 3 and the numbers strictly increase to a single peak,
# then strictly decrease to the end.
#
# Example 1:
# Input:  arr = [0, 3, 2, 1]
# Output: True  # Uphill 0 -> 3, downhill 3 -> 2 -> 1
#
# Example 2:
# Input:  arr = [3, 5, 5]
# Output: False  # Plateau / duplicate numbers not allowed
#
# Example 3 (Edge Case):
# Input:  arr = [2, 1]
# Output: False  # Length must be at least 3
#
# Think About:
# - Two climbers starting from opposite ends:
#   * Left climber starts at left = 0, climbs uphill while left + 1 < len(arr) and arr[left] < arr[left + 1].
#   * Right climber starts at right = len(arr) - 1, climbs uphill while right - 1 >= 0 and arr[right] < arr[right - 1].
# - If both climbers meet at exact same peak (left == right) and peak is not index 0 and not last index, return True!
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below


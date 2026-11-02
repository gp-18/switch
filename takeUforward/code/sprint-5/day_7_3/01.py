# Floor and Ceil in Sorted Array
# Given a sorted array nums and an integer x. Find the floor and ceil of x.
# Floor: largest element in nums <= x (or -1 if none).
# Ceil: smallest element in nums >= x (or -1 if none).
#
# Example 1:
# Input:  nums = [3, 4, 4, 7, 8, 10], x = 5
# Output: [4, 7]
#
# Example 2:
# Input:  nums = [3, 4, 4, 7, 8, 10], x = 8
# Output: [8, 8]
#
# Example 3:
# Input:  nums = [2, 4, 6, 8, 10, 12, 14], x = 1
# Output: [-1, 2]
#
# Think About:
# - Floor: If nums[mid] <= x: floor = nums[mid], search right (low = mid + 1).
#          Else: search left (high = mid - 1).
# - Ceil:  If nums[mid] >= x: ceil = nums[mid], search left (high = mid - 1).
#          Else: search right (low = mid + 1).
# - Time Complexity: O(log N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

x = int(input("Enter integer x : "))

print(f"Your sorted array : {array} with x = {x}")

# Write your solution below:
# Optimal Approach: Binary Search for Floor and Ceil
# Time Complexity: O(log N) | Space Complexity: O(1)

def find_floor(nums, target):
    low, high = 0, len(nums) - 1
    ans = -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] <= target:
            ans = nums[mid]
            # Try finding a larger element <= target on the right
            low = mid + 1
        else:
            high = mid - 1
    return ans

def find_ceil(nums, target):
    low, high = 0, len(nums) - 1
    ans = -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] >= target:
            ans = nums[mid]
            # Try finding a smaller element >= target on the left
            high = mid - 1
        else:
            low = mid + 1
    return ans

floor_val = find_floor(array, x)
ceil_val = find_ceil(array, x)

print(f"Floor of {x} : {floor_val}")
print(f"Ceil of {x}  : {ceil_val}")
print(f"Result [floor, ceil] : [{floor_val}, {ceil_val}]")

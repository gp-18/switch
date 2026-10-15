# Move Negative Numbers to Front, Positives to Back
# Given an array nums of positive and negative integers, rearrange the array in-place
# so that all negative numbers appear on the left and all positive numbers appear on the right.
# Any order inside each group is fine.
#
# Example 1:
# Input:  nums = [3, -1, 4, -5, 2]
# Output: [-1, -5, 4, 3, 2]  # Any order where negatives are on the left
#
# Example 2:
# Input:  nums = [-2, -3, 4, -1, 5]
# Output: [-2, -3, -1, 4, 5]
#
# Example 3 (Edge Case):
# Input:  nums = [-4, -2, -1]
# Output: [-4, -2, -1]  # Already all negative
#
# Think About:
# - Put left = 0 and right = len(nums) - 1.
# - Advance left while nums[left] < 0.
# - Decrement right while nums[right] >= 0.
# - When left < right: swap nums[left] and nums[right].
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

start = 0 
for i in range(len(array)) : 
    if array[i] < 0 : 
        array[start], array[i] = array[i], array[start] 
        start += 1 

print("Array after moving negative numbers to front : ", array)


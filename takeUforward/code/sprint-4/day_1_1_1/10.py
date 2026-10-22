# Segregate 0s and 1s in an Array
# Given a binary array nums containing only 0s and 1s, sort the array in-place
# so that all 0s are on the left and all 1s are on the right.
#
# Example 1:
# Input:  nums = [0, 1, 0, 1, 1, 0]
# Output: [0, 0, 0, 1, 1, 1]
#
# Example 2:
# Input:  nums = [1, 1, 0, 0, 1]
# Output: [0, 0, 1, 1, 1]
#
# Example 3 (Edge Case):
# Input:  nums = [1, 1, 1]
# Output: [1, 1, 1]  # No zeros present
#
# Think About:
# - Put left = 0 and right = len(nums) - 1.
# - Advance left while nums[left] == 0 (left += 1).
# - Decrement right while nums[right] == 1 (right -= 1).
# - When left < right: swap nums[left] and nums[right].
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the binary array : "))
array = []

for i in range(length):
    value = int(input(f"Enter binary value (0 or 1) at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below


start = 0 

for i in range(len(array)) :

    if array[i] == 0 : 
        array[start], array[i] = array[i], array[start]
        start += 1 

print("Array after segregation : ", array)

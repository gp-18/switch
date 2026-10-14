# Count Pairs with Given Sum in a Sorted Array
# Given an array of distinct integers nums sorted in ascending order, and an integer target,
# count how many unique pairs (nums[i], nums[j]) with i < j add up to target.
#
# Example 1:
# Input:  nums = [1, 2, 3, 4, 5, 6], target = 7
# Output: 3  # Pairs: (1, 6), (2, 5), (3, 4)
#
# Example 2:
# Input:  nums = [1, 3, 5, 7, 9], target = 12
# Output: 2  # Pairs: (3, 9), (5, 7)
#
# Example 3 (Edge Case):
# Input:  nums = [2, 4, 6], target = 15
# Output: 0  # No pair sums to 15
#
# Think About:
# - Initialize left = 0, right = len(nums) - 1, and count = 0.
# - While left < right:
#   * If nums[left] + nums[right] == target: count += 1, left += 1, right -= 1.
#   * If nums[left] + nums[right] < target: left += 1.
#   * If nums[left] + nums[right] > target: right -= 1.
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

target = int(input("Enter the target sum : "))

print(f"Your array has become : {array}, target is : {target} and now doing the operations on it.")

# Write your solution below

low_index = 0 
high_index = len(array) - 1 

count = 0 

while low_index < high_index : 

    current_sum = array[low_index] + array[high_index]

    if current_sum == target: 
        count += 1
        low_index += 1
        high_index -= 1 
        
    elif current_sum < target : 
        low_index += 1
        
    else :
        high_index -= 1 

print(f"Count of pairs : {count}")
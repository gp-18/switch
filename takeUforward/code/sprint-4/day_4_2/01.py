# Sort an Array of 0's, 1's, and 2's (Dutch National Flag Algorithm)
# Given an array nums consisting of only 0, 1, or 2, sort the array in non-decreasing order.
# The sorting must be done in-place, without making a copy of the original array.
#
# Example 1:
# Input:  nums = [1, 0, 2, 1, 0]
# Output: [0, 0, 1, 1, 2]
# Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two.
#
# Example 2:
# Input:  nums = [0, 0, 1, 1, 1]
# Output: [0, 0, 1, 1, 1]
# Explanation: The nums array in sorted order has 2 zeroes, 3 ones and zero twos.
#
# Example 3 (Edge Case):
# Input:  nums = [2, 0, 1]
# Output: [0, 1, 2]
#
# Think About:
# - Optimal Approach (Dutch National Flag Algorithm):
#   - Use 3 pointers: low = 0, mid = 0, high = n - 1
#   - Partitions:
#       [0 ... low - 1]      -> all 0s
#       [low ... mid - 1]    -> all 1s
#       [mid ... high]       -> unsorted (0s, 1s, 2s)
#       [high + 1 ... n - 1] -> all 2s
#   - While mid <= high:
#       * If nums[mid] == 0: swap(nums[low], nums[mid]), low += 1, mid += 1
#       * If nums[mid] == 1: mid += 1
#       * If nums[mid] == 2: swap(nums[mid], nums[high]), high -= 1 (do NOT increment mid)
# - Time Complexity: O(N) single pass
# - Space Complexity: O(1) in-place
#

length = int(input("Enter the length of the array: "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} (0, 1, or 2): "))
    array.append(value)

print(f"Your array has become: {array} and now doing the operations on it.")

# Write your solution below

low  , mid , high = 0 , 0 , len(array) - 1 

while mid <= high : 

    if array[mid] == 0 : 
        array[low] , array[mid] = array[mid] , array[low]
        low += 1
        mid += 1 
    elif array[mid] == 1 : 
        mid += 1
    else : 
        array[mid] , array[high] = array[high] , array[mid] 
        high -= 1

print(f"Sorted array: {array}")
        
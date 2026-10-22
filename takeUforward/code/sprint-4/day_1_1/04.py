# Sum of Mirror Pairs (Ends to Middle)
# Given an array of integers nums, calculate the sum of pairs starting from both ends:
# add the first and last element, then the second and second-last element, and so on.
# Return these sums in a list. If the array has an odd length, include the middle single element alone at the end.
#
# Example 1:
# Input:  nums = [1, 2, 3, 4, 5]
# Output: [6, 6, 3]  # (1 + 5 = 6), (2 + 4 = 6), middle 3
#
# Example 2:
# Input:  nums = [10, 20, 30, 40]
# Output: [50, 50]  # (10 + 40 = 50), (20 + 30 = 50)
#
# Example 3 (Edge Case):
# Input:  nums = [9]
# Output: [9]  # Single element middle
#
# Think About:
# - Initialize left = 0, right = len(nums) - 1, and result = [].
# - While left < right:
#   * Append nums[left] + nums[right] to result.
#   * Move left += 1 and right -= 1.
# - If left == right after loop (odd length), append nums[left].
# - Time Complexity: O(N)
# - Space Complexity: O(N) for output list
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

low = 0 
high = len(array) - 1
result_list = []

while low < high :
    
    result_list.append(array[low] + array[high])
    
    low += 1
    high -= 1

if low == high:
    result_list.append(array[low])

print(f"Resultant list : {result_list}")
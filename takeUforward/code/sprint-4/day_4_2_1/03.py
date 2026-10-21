# Three-Way Partitioning Around a Given Pivot
# Given an integer array nums and a value pivot, rearrange nums in-place such that:
#   1. All elements less than pivot appear first.
#   2. All elements equal to pivot appear in the middle.
#   3. All elements greater than pivot appear at the end.
#
# Example 1:
# Input:  nums = [9, 12, 5, 10, 14, 3, 10], pivot = 10
# Output: [9, 5, 3, 10, 10, 14, 12]
#
# Example 2:
# Input:  nums = [-3, 4, 3, 2], pivot = 2
# Output: [-3, 2, 4, 3]
#
# Example 3 (Edge Case):
# Input:  nums = [7, 7, 7], pivot = 7
# Output: [7, 7, 7]  # All elements equal to pivot
#
# Think About:
# - Dutch National Flag general form:
#   * low = 0, mid = 0, high = n - 1
#   * While mid <= high:
#       - If nums[mid] < pivot: swap nums[low] and nums[mid], low += 1, mid += 1
#       - If nums[mid] == pivot: mid += 1
#       - If nums[mid] > pivot: swap nums[mid] and nums[high], high -= 1 (do NOT increment mid)
# - Time Complexity: O(N) single pass
# - Space Complexity: O(1) in-place
#

length = int(input("Enter the length of the array: "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i}: "))
    array.append(value)

pivot = int(input("Enter the pivot value: "))

print(f"Your array has become: {array}, pivot is: {pivot} and now doing the operations on it.")

# Write your solution below

low , mid , high = 0 , 0 , len(array) - 1 


while mid <= high : 
    if array[mid] < pivot : 
        array[low] , array[mid] = array[mid] , array[low] 
        low += 1 
        mid += 1 
    elif array[mid] > pivot : 
        array[mid] , array[high] = array[high] , array[mid] 
        high -= 1 
    else : 
        mid += 1 

print(array)
    
    
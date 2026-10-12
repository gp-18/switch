# Linear Search
# Given an array of integers nums and an integer target k, find the index of k in nums.
# If k is present, return its 0-based index; otherwise, return -1.
#
# Example 1:
# Input:  nums = [1, 2, 3, 4, 5], k = 3
# Output: 2
#
# Example 2:
# Input:  nums = [5, 4, 3, 2, 1], k = 6
# Output: -1
#
# Think About:
# - Scan sequentially from index 0 to n - 1.
# - Early return as soon as nums[i] == k is matched.
# - Time Complexity: O(N) worst/average case, O(1) best case.
# - Space Complexity: O(1) auxiliary space.
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

k = int(input("Enter the target element k to search : "))

print(f"Your array has become : {array}, target is : {k} and now doing the operations on it.")

def linear_search(nums, target):
    """
    Search for target in nums using the Linear Search algorithm.
    Iterates sequentially through each element until target is found.
    
    Time Complexity:
    - Best Case: O(1) (target is at the first index)
    - Average/Worst Case: O(N) (target is at the end or absent)
    Space Complexity: O(1) (no extra memory used)
    """
    # Traverse through all elements from index 0 to len(nums) - 1
    for i in range(len(nums)):
        # Check if the current element matches the target
        if nums[i] == target:
            # Match found! Return the 0-based index immediately
            return i
            
    # If the loop finishes without finding the target, it does not exist
    return -1


# Call the function and display the result
index = linear_search(array, k)

if index != -1:
    print(f"Result: Element {k} found at index {index}.")
else:
    print(f"Result: Element {k} not found in the array (returned {index}).")



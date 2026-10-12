# Largest Element
# Given an array nums of N integers, find and return the largest element in the array.
#
# Example 1:
# Input:  nums = [2, 5, 1, 3, 0]
# Output: 5
#
# Example 2:
# Input:  nums = [8, 10, 5, 7, 9]
# Output: 10
#
# Think About:
# - Initialize max_val = nums[0].
# - Iterate through nums from index 1 to N - 1: if nums[i] > max_val, update max_val = nums[i].
# - Avoid sorting the array (O(N log N)); a single pass runs in O(N) time.
# - Time Complexity: O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

def find_largest_element(nums):
    """
    Find and return the largest element in the array using a single linear scan.
    
    Why not sort first?
    Sorting takes O(N log N) time, whereas a single pass takes only O(N) time.
    
    Time Complexity: O(N) (we inspect each element once)
    Space Complexity: O(1) (only one variable max_val is stored)
    """
    # Edge case: If array is empty
    if not nums:
        return None

    # Step 1: Assume the first element is the largest so far
    max_val = nums[0]

    # Step 2: Iterate through the rest of the array starting from index 1
    for i in range(1, len(nums)):
        # If the current element is greater than our current max_val, update it
        if nums[i] > max_val:
            max_val = nums[i]

    # Step 3: Return the largest element found
    return max_val


# Call the function and display the result
largest = find_largest_element(array)
print(f"Result: Largest element in the array is: {largest}")



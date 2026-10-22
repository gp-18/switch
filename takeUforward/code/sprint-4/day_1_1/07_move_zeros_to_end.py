# Move Zeros to End
# Given an integer array nums, move all 0s to the end of the array while maintaining the relative order of non-zero elements in-place.
#
# Example 1:
# Input:  nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
#
# Example 2:
# Input:  nums = [0, 0, 1]
# Output: [1, 0, 0]
#
# Think About:
# - Find the index j of the first zero in the array. If no zero exists, return.
# - Loop pointer i from j + 1 to N - 1:
#   * Whenever nums[i] != 0: swap nums[i] with nums[j], then increment j += 1.
# - All non-zeros stay in relative order, and zeros naturally slide to the back.
# - Time Complexity: O(N)
# - Space Complexity: O(1) in-place.
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

def move_zeros_to_end(nums):
    """
    Move all 0s to the end of nums in-place while keeping non-zeros in relative order.
    
    Two-Pointer Logic:
    1. Find the index `j` of the first 0.
       If there is no 0 in the entire array, nothing needs to move!
    2. Iterate `i` from `j + 1` to `N - 1`:
       - If nums[i] is non-zero, swap nums[i] with nums[j].
       - Increment `j` by 1. Now nums[j] is once again pointing to a 0 ready for the next non-zero.
       
    Time Complexity: O(N) (at most one full traversal to find first zero + one traversal to swap)
    Space Complexity: O(1) in-place auxiliary space
    """
    n = len(nums)
    if n <= 1:
        return nums

    # Step 1: Locate the index of the first zero
    j = -1
    for idx in range(n):
        if nums[idx] == 0:
            j = idx
            break

    # If no zeros are present, array is already in required order
    if j == -1:
        return nums

    # Step 2: Swap subsequent non-zero elements with the zero at index j
    for i in range(j + 1, n):
        if nums[i] != 0:
            # Swap non-zero element with the zero at index j
            nums[i], nums[j] = nums[j], nums[i]
            # Advance j to the next zero
            j += 1

    return nums


# Call the function (modifies the array in-place) and display the result
result = move_zeros_to_end(array)
print(f"Result: Array after moving zeros to end: {result}")



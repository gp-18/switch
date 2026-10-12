# Left Rotate Array by One
# Given an array nums of N integers, rotate the array to the left by one position in-place.
#
# Example 1:
# Input:  nums = [1, 2, 3, 4, 5]
# Output: [2, 3, 4, 5, 1]
#
# Example 2:
# Input:  nums = [3]
# Output: [3]
#
# Think About:
# - Store the first element temp = nums[0].
# - Shift elements from index 1 to N - 1 one place to the left: nums[i - 1] = nums[i].
# - Place temp at the last index: nums[N - 1] = temp.
# - Time Complexity: O(N)
# - Space Complexity: O(1) extra space.
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

def left_rotate_by_one(nums):
    """
    Rotate the given array to the left by one position in-place.
    
    Approach:
    1. If the array is empty or has only 1 element, no rotation needed.
    2. Save the first element nums[0] in a temporary variable `temp`.
    3. Shift each element from index 1 to N - 1 leftward by 1 position (nums[i - 1] = nums[i]).
    4. Place `temp` into the last position (nums[N - 1]).
    
    Time Complexity: O(N) (shifts N - 1 elements)
    Space Complexity: O(1) in-place (uses only 1 temporary variable)
    """
    n = len(nums)
    # Edge case: If array has 0 or 1 element, rotation leaves it identical
    if n <= 1:
        return nums

    # Step 1: Save the first element before it gets overwritten
    temp = nums[0]

    # Step 2: Shift all subsequent elements one place to the left
    for i in range(1, n):
        nums[i - 1] = nums[i]

    # Step 3: Put the saved first element into the last index
    nums[n - 1] = temp

    return nums


# Call the function (modifies the array in-place) and display the result
rotated = left_rotate_by_one(array)
print(f"Result: Array after left rotation by 1: {rotated}")



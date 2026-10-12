# Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove duplicates in-place
# such that each unique element appears only once. Return the number of unique elements k.
#
# Example 1:
# Input:  nums = [1, 1, 2]
# Output: k = 2, nums = [1, 2, _]
#
# Example 2:
# Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: k = 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
#
# Think About:
# - Use two pointers: i = 0 tracks the index of the last placed unique element.
# - Pointer j iterates from 1 to N - 1:
#   * If nums[j] != nums[i]: increment i += 1 and set nums[i] = nums[j].
# - The number of unique elements is i + 1.
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space.
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

def remove_duplicates(nums):
    """
    Remove duplicates in-place from a sorted array nums.
    Returns the count of unique elements `k`. The first `k` elements of nums
    will hold the unique elements in sorted order.
    
    Two-Pointer Strategy (Reader & Writer):
    - `i` (Writer pointer): Points to the last recognized unique element. Starts at 0.
    - `j` (Reader pointer): Scans through indices 1 to N - 1.
    - If nums[j] != nums[i]:
        nums[j] is a newly discovered distinct value.
        Advance `i += 1` and write `nums[i] = nums[j]`.
    - If nums[j] == nums[i]:
        It's a duplicate of the current unique element, so skip it (only reader `j` advances).
    
    Time Complexity: O(N) (reader visits each index once)
    Space Complexity: O(1) auxiliary space (in-place modification)
    """
    n = len(nums)
    if n == 0:
        return 0

    # Pointer i keeps track of the index of the last placed unique element
    i = 0

    # Pointer j scans forward from index 1 to n - 1
    for j in range(1, n):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    # Number of unique elements is i + 1 (since 0-indexed)
    return i + 1


# Call the function (modifies the array in-place) and display the result
k = remove_duplicates(array)
print(f"Result: Number of unique elements (k) = {k}")
print(f"Unique elements portion of the array: {array[:k]}")



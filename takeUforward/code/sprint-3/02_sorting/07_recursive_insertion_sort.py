# Recursive Insertion Sort
# Insertion Sort implemented using recursion instead of an outer loop.
# In each recursive call:
# 1. Base case: When index `i == n`, the whole array has been processed.
# 2. Pick `key = nums[i]`.
# 3. Shift elements in nums[0 ... i - 1] that are strictly greater than `key` to the right.
# 4. Insert `key` at the correct position.
# 5. Recurse for the next index `i + 1`.
#
# Time Complexity:
# - Best Case:    O(N)   (When already sorted)
# - Average Case: O(N^2)
# - Worst Case:   O(N^2)
# Space Complexity: O(N) (Recursion call stack space)
# Stability: Stable
#
# Example 1:
# Input:  nums = [13, 46, 24, 52, 20, 9]
# Output: [9, 13, 20, 24, 46, 52]
#
# Example 2:
# Input:  nums = [1, 2, 3, 4, 5]
# Output: [1, 2, 3, 4, 5]
#
# Example 3 (Edge Case - Duplicates & Negatives):
# Input:  nums = [5, -2, 3, -2, 0, 8]
# Output: [-2, -2, 0, 3, 5, 8]

length = int(input("Enter the length of the array : "))
array = []

for i in range(0, length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")


def recursive_insertion_sort(nums, i, n):
    """
    Recursively sorts nums by inserting nums[i] into the sorted prefix nums[0 ... i - 1].
    """
    # Base case: all elements from index 1 to n - 1 have been inserted
    if i >= n:
        return nums

    key = nums[i]
    j = i - 1

    # Shift elements strictly greater than key one position to the right
    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1

    # Insert key into its correct position
    nums[j + 1] = key

    # Recurse for the next element at index i + 1
    return recursive_insertion_sort(nums, i + 1, n)


sorted_array = recursive_insertion_sort(array, 1, len(array))
print(f"Sorted array : {sorted_array}")

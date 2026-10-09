# Recursive Bubble Sort
# Bubble Sort implemented using recursion instead of an outer loop.
# In each recursive call:
# 1. One pass is made over the array of size `n`, pushing the maximum element to the end (index `n - 1`).
# 2. Recurse for the remaining subarray of size `n - 1`.
# 3. Base case: When size `n == 1`, the array is sorted.
#
# Time Complexity:
# - Best Case:    O(N)   (With early exit swapped check)
# - Average Case: O(N^2)
# - Worst Case:   O(N^2)
# Space Complexity: O(N) (Recursion call stack space)
# Stability: Stable
#
# Example 1:
# Input:  nums = [5, 3, 8, 4, 2]
# Output: [2, 3, 4, 5, 8]
#
# Example 2:
# Input:  nums = [1, 2, 3, 4, 5]
# Output: [1, 2, 3, 4, 5]
#
# Example 3 (Edge Case - Duplicates & Negatives):
# Input:  nums = [3, -1, 4, -1, 5, 2]
# Output: [-1, -1, 2, 3, 4, 5]

length = int(input("Enter the length of the array : "))
array = []

for i in range(0, length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")


def recursive_bubble_sort(nums, n):
    """
    Recursively sorts nums[0 ... n - 1].
    Each call moves the largest element among the first n elements to index n - 1.
    """
    # Base case: an array of size 1 or 0 is already sorted
    if n <= 1:
        return nums

    swapped = False

    # One pass of bubble sort for the first n elements
    for j in range(n - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swapped = True

    # If no elements were swapped, the array is already sorted
    if not swapped:
        return nums

    # Recurse for the remaining n - 1 elements
    return recursive_bubble_sort(nums, n - 1)


sorted_array = recursive_bubble_sort(array, len(array))
print(f"Sorted array : {sorted_array}")

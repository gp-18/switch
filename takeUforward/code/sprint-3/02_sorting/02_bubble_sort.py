# Bubble Sort (with Early Termination Optimization)
# Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.
# The largest element gradually "bubbles up" to the end of the array after each pass.
#
# Optimization:
# If no swaps occur in a pass, the array is already sorted, so we break early.
#
# Time Complexity:
# - Best Case:    O(N)   (When array is already sorted, stops after 1 pass)
# - Average Case: O(N^2)
# - Worst Case:   O(N^2) (When array is reverse sorted)
# Space Complexity: O(1) (In-place)
# Stability: Stable (Equal elements are not swapped when using `>`)
#
# Example 1:
# Input:  nums = [5, 3, 8, 4, 2]
# Output: [2, 3, 4, 5, 8]
#
# Example 2:
# Input:  nums = [1, 2, 3, 4, 5]
# Output: [1, 2, 3, 4, 5]
#
# Example 3 (Edge Case - Negative & Duplicates):
# Input:  nums = [6, -2, 4, 0, -2, 8]
# Output: [-2, -2, 0, 4, 6, 8]

length = int(input("Enter the length of the array : "))
array = []

for i in range(0, length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")


def bubble_sort(nums):
    n = len(nums)

    # Outer loop for passes: runs at most n - 1 times (i from 0 to n - 2).
    # After pass i, the (i + 1) largest elements are settled at the right end.
    for i in range(n - 1):
        swapped = False

        # Inner loop for adjacent comparisons:
        # We compare nums[j] with nums[j + 1].
        # The limit is (n - 1 - i) because:
        # 1. '- 1' avoids index out of range when accessing nums[j + 1].
        # 2. '- i' avoids re-checking the last i elements which are already sorted.
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                # Swap adjacent elements if left is strictly greater than right
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        # Optimization: If no two elements were swapped in this pass,
        # the array is already sorted, so we can terminate early.
        if not swapped:
            break

    return nums


sorted_array = bubble_sort(array)
print(f"Sorted array : {sorted_array}")

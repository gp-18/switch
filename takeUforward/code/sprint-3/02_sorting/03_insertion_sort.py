# Insertion Sort
# Insertion Sort builds the sorted array one element at a time.
# At each step:
# 1. Pick the current element as `key`.
# 2. Compare `key` with elements to its left in the sorted portion.
# 3. Shift all elements greater than `key` one position to the right.
# 4. Insert `key` into its correct sorted position.
#
# Time Complexity:
# - Best Case:    O(N)   (When array is already sorted, only 1 check per element)
# - Average Case: O(N^2)
# - Worst Case:   O(N^2) (When array is reverse sorted)
# Space Complexity: O(1) (In-place)
# Stability: Stable (Strictly greater condition `nums[j] > key` preserves duplicate order)
#
# Example 1:
# Input:  nums = [13, 46, 24, 52, 20, 9]
# Output: [9, 13, 20, 24, 46, 52]
#
# Example 2:
# Input:  nums = [1, 2, 3, 4, 5]
# Output: [1, 2, 3, 4, 5]
#
# Example 3 (Edge Case - Negative & Duplicates):
# Input:  nums = [-4, 5, 10, -4, 2, 0]
# Output: [-4, -4, 0, 2, 5, 10]

length = int(input("Enter the length of the array : "))
array = []

for i in range(0, length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")


def insertion_sort(nums):
    n = len(nums)

    # Start from index 1 because a single element at index 0 is already sorted by definition.
    for i in range(1, n):
        # `key` is the value we want to insert into the sorted subarray nums[0...i-1].
        key = nums[i]

        # `j` starts from the element immediately to the left of `key`.
        j = i - 1

        # Shift elements of nums[0...i-1] that are strictly greater than `key`
        # one position to the right to make space for `key`.
        # Condition `j >= 0` avoids underflow.
        # Condition `nums[j] > key` stops as soon as an element <= key is found.
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]  # Shift element right
            j -= 1                 # Move pointer left

        # Insert `key` into the vacated slot (j + 1).
        nums[j + 1] = key

    return nums


sorted_array = insertion_sort(array)
print(f"Sorted array : {sorted_array}")

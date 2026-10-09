# Selection Sort
# Selection Sort works by dividing the array into two parts: [Sorted part | Unsorted part].
# At every step:
# 1. Find the smallest (minimum) element in the unsorted part.
# 2. Swap it with the element at the beginning of the unsorted part.
# 3. Move the boundary forward and repeat until the array is sorted.
#
# Time Complexity:
# - Best Case:    O(N^2)
# - Average Case: O(N^2)
# - Worst Case:   O(N^2)
# Space Complexity: O(1) (In-place)
# Stability: Unstable (Standard version)
#
# Example 1:
# Input:  nums = [64, 25, 12, 22, 11]
# Output: [11, 12, 22, 25, 64]
#
# Example 2:
# Input:  nums = [5, 4, 3, 2, 1]
# Output: [1, 2, 3, 4, 5]
#
# Example 3 (Edge Case - Negative & Duplicates):
# Input:  nums = [3, -1, 4, -1, 5, 2]
# Output: [-1, -1, 2, 3, 4, 5]

length = int(input("Enter the length of the array : "))
array = []

for i in range(0, length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")


def selection_sort(nums):
    n = len(nums)

    # Outer loop moves the boundary of the unsorted subarray.
    # We only need to go up to n - 2 because when n - 1 elements are sorted,
    # the last element is guaranteed to be in its correct place.
    for i in range(n - 1):

        # Assume the current element at index i is the minimum.
        min_index = i

        # Inner loop searches for the actual minimum in the unsorted portion (i + 1 to n - 1).
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        # If a smaller element was found, swap it with the element at index i.
        # This places the minimum element at its correct sorted position.
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


sorted_array = selection_sort(array)
print(f"Sorted array : {sorted_array}")

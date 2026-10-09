# Quick Sort
# Quick Sort is a Divide and Conquer algorithm.
# 1. Pick a pivot element (e.g., the first element `arr[low]`).
# 2. Partition: Rearrange the array such that:
#    - All elements smaller than or equal to the pivot are on the left.
#    - All elements greater than the pivot are on the right.
#    - The pivot is placed at its correct sorted position (partition index `p_index`).
# 3. Recursively apply Quick Sort to the left and right subarrays.
#
# Time Complexity:
# - Best Case:    O(N log N) (Pivot divides array roughly in half)
# - Average Case: O(N log N)
# - Worst Case:   O(N^2)     (When array is already sorted/reverse-sorted and pivot is extreme)
# Space Complexity: O(log N) (Recursion call stack space)
# Stability: Unstable (Swapping over long distances can alter duplicate element order)
#
# Example 1:
# Input:  nums = [4, 6, 2, 5, 7, 9, 1, 3]
# Output: [1, 2, 3, 4, 5, 6, 7, 9]
#
# Example 2:
# Input:  nums = [5, 4, 3, 2, 1]
# Output: [1, 2, 3, 4, 5]
#
# Example 3 (Edge Case - Duplicates & Negatives):
# Input:  nums = [-2, 4, 0, -2, 5, 1]
# Output: [-2, -2, 0, 1, 4, 5]

length = int(input("Enter the length of the array : "))
array = []

for i in range(0, length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")


def partition(arr, low, high):
    """
    Partitions subarray arr[low ... high] around the pivot arr[low].
    Places elements <= pivot to left, and elements > pivot to right.
    Returns the final sorted index of the pivot.
    """
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        # Move `i` forward until finding an element strictly greater than pivot
        while arr[i] <= pivot and i <= high - 1:
            i += 1

        # Move `j` backward until finding an element smaller than or equal to pivot
        while arr[j] > pivot and j >= low + 1:
            j -= 1

        # If pointers haven't crossed, swap out-of-place elements
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Swap pivot into its correct sorted position (index j)
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort_helper(arr, low, high):
    """
    Recursively sorts subarray arr[low ... high].
    """
    if low < high:
        # Find partition index
        p_index = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort_helper(arr, low, p_index - 1)
        quick_sort_helper(arr, p_index + 1, high)


def quick_sort(nums):
    n = len(nums)
    if n > 1:
        quick_sort_helper(nums, 0, n - 1)
    return nums


sorted_array = quick_sort(array)
print(f"Sorted array : {sorted_array}")

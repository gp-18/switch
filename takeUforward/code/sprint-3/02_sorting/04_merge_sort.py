# Merge Sort
# Merge Sort is a Divide and Conquer algorithm.
# 1. Divide: Split the array into two halves at the midpoint until each subarray has 1 element.
# 2. Sort: A single element is already sorted (base case: low >= high).
# 3. Merge: Combine two sorted adjacent halves using a two-pointer technique into a sorted whole.
#
# Time Complexity:
# - Best Case:    O(N log N)
# - Average Case: O(N log N)
# - Worst Case:   O(N log N)
# Space Complexity: O(N) (Auxiliary space for temp array + O(log N) recursion call stack)
# Stability: Stable (Using `<=` in merge prioritizes the left element for equal values)
#
# Example 1:
# Input:  nums = [9, 4, 7, 6, 3, 1, 5]
# Output: [1, 3, 4, 5, 6, 7, 9]
#
# Example 2:
# Input:  nums = [5, 4, 3, 2, 1]
# Output: [1, 2, 3, 4, 5]
#
# Example 3 (Edge Case - Negative & Duplicates):
# Input:  nums = [10, -1, 2, 5, 2, -1, 0]
# Output: [-1, -1, 0, 2, 2, 5, 10]

length = int(input("Enter the length of the array : "))
array = []

for i in range(0, length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")


def merge(arr, low, mid, high):
    """
    Combines two adjacent sorted subarrays:
    Left:  arr[low ... mid]
    Right: arr[mid + 1 ... high]
    """
    temp = []
    left = low        # Pointer for the left sorted subarray
    right = mid + 1   # Pointer for the right sorted subarray

    # Compare elements from both halves and append the smaller to temp
    while left <= mid and right <= high:
        # Using '<=' ensures stability: equal elements from left half are picked first
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # Copy remaining elements from the left subarray (if any)
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Copy remaining elements from the right subarray (if any)
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy merged elements from temp back into the original array arr[low ... high]
    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def merge_sort_helper(arr, low, high):
    """
    Recursively divides array into two halves until single elements, then merges them.
    """
    # Base case: 1 element (low == high) or invalid range (low > high)
    if low >= high:
        return

    mid = (low + high) // 2

    # Recursively sort left and right halves
    merge_sort_helper(arr, low, mid)
    merge_sort_helper(arr, mid + 1, high)

    # Merge the two sorted halves
    merge(arr, low, mid, high)


def merge_sort(nums):
    n = len(nums)
    if n > 1:
        merge_sort_helper(nums, 0, n - 1)
    return nums


sorted_array = merge_sort(array)
print(f"Sorted array : {sorted_array}")

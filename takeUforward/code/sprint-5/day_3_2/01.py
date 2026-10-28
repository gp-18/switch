# Reverse Pairs
# Given an integer array nums. Return the number of reverse pairs in the array.
# An index pair (i, j) is called a reverse pair if 0 <= i < j < len(nums) and nums[i] > 2 * nums[j].
#
# Example 1:
# Input:  nums = [6, 4, 1, 2, 7]
# Output: 3
# Explanation: (0, 2), (0, 3), (1, 2) form reverse pairs.
#
# Example 2:
# Input:  nums = [5, 4, 4, 3, 3]
# Output: 0
#
# Example 3:
# Input:  nums = [6, 4, 4, 2, 2]
# Output: 2
# Explanation: (0, 3) and (0, 4) form reverse pairs.
#
# Think About:
# - Two-Pass Modified Merge Sort:
#   * In standard Count Inversions, counting happens during merging.
#   * For nums[i] > 2 * nums[j], merge order differs from pair condition.
#   * Solution: First count pairs using two pointers across sorted halves in O(N).
#   * Then merge the sorted halves in O(N).
# - Time Complexity: O(2N log N) ≈ O(N log N)
# - Space Complexity: O(N) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below:

# Optimal Approach: Modified Merge Sort with Decoupled Two-Pointer Counting
# Time Complexity: O(N log N) | Space Complexity: O(N)

def count_pairs(arr, low, mid, high):
    cnt = 0
    right = mid + 1

    # Traverse left sorted half
    for i in range(low, mid + 1):
        # Advance right pointer as long as condition holds
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        # Add count of qualifying elements from right half
        cnt += (right - (mid + 1))

    return cnt


def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    # Standard merge of two sorted halves
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy merged elements back into original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def merge_sort(arr, low, high):
    cnt = 0
    if low < high:
        mid = (low + high) // 2
        # Count reverse pairs in left half
        cnt += merge_sort(arr, low, mid)
        # Count reverse pairs in right half
        cnt += merge_sort(arr, mid + 1, high)
        # Count reverse pairs across left and right halves
        cnt += count_pairs(arr, low, mid, high)
        # Merge the two sorted halves
        merge(arr, low, mid, high)
    return cnt


total_reverse_pairs = merge_sort(array, 0, len(array) - 1)
print(f"The number of reverse pairs are: {total_reverse_pairs}")

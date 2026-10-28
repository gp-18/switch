# Count Inversions
# Given an integer array nums. Return the number of inversions in the array.
# Two elements nums[i] and nums[j] form an inversion if nums[i] > nums[j] and i < j.
#
# Example 1:
# Input:  nums = [2, 3, 7, 1, 3, 5]
# Output: 5
# Explanation: (2, 1), (3, 1), (7, 1), (7, 3), (7, 5) form inversions.
#
# Example 2:
# Input:  nums = [-10, -5, 6, 11, 15, 17]
# Output: 0
# Explanation: Array is sorted, so 0 inversions.
#
# Think About:
# - Modified Merge Sort:
#   * Divide array into left (low..mid) and right (mid+1..high) halves.
#   * When merging two sorted halves:
#     - If arr[left] <= arr[right]: no inversion, advance left.
#     - If arr[left] > arr[right]: all remaining elements in left half (mid - left + 1)
#       are strictly greater than arr[right]. Add (mid - left + 1) to cnt.
# - Time Complexity: O(N log N)
# - Space Complexity: O(N) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below:

# Optimal Approach: Divide & Conquer (Modified Merge Sort)
# Time Complexity: O(N log N) | Space Complexity: O(N)

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    cnt = 0

    # Merge two sorted halves while counting split inversions
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            # All elements from left to mid form inversions with arr[right]
            cnt += (mid - left + 1)
            right += 1

    # Copy remaining elements of left half
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Copy remaining elements of right half
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy merged elements back into original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return cnt


def merge_sort(arr, low, high):
    cnt = 0
    if low < high:
        mid = (low + high) // 2
        # Count inversions in left half
        cnt += merge_sort(arr, low, mid)
        # Count inversions in right half
        cnt += merge_sort(arr, mid + 1, high)
        # Count split inversions across left and right halves
        cnt += merge(arr, low, mid, high)
    return cnt


total_inversions = merge_sort(array, 0, len(array) - 1)
print(f"The number of inversions are: {total_inversions}")

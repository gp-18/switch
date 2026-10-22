# Left Rotate Array by K Places
# Given an array nums of N integers and an integer k, rotate the array to the left by k places.
#
# Example 1:
# Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 2
# Output: [3, 4, 5, 6, 7, 1, 2]
#
# Example 2:
# Input:  nums = [3, 7, 8, 9], k = 3
# Output: [9, 3, 7, 8]
#
# Think About:
# - Normalize k = k % N since rotating by N returns to the original array.
# - Optimal Reversal Algorithm (O(1) extra space):
#   1. Reverse the first k elements: reverse(0, k - 1)
#   2. Reverse the remaining N - k elements: reverse(k, N - 1)
#   3. Reverse the entire array: reverse(0, N - 1)
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space.
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

k = int(input("Enter the number of places k to rotate left : "))

print(f"Your array has become : {array}, k is : {k} and now doing the operations on it.")

def reverse_subarray(nums, start, end):
    """
    Helper function to reverse elements of nums from index `start` to `end` in-place
    using two opposite-end pointers.
    """
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def left_rotate_by_k(nums, k):
    """
    Rotates array nums to the left by k positions in-place using the Optimal Reversal Algorithm.
    
    How it works:
    Let nums = [1, 2, 3, 4, 5, 6, 7] and k = 2:
    - Step 1: Reverse first k elements (index 0 to k-1):
              [1, 2] -> [2, 1], array becomes [2, 1, 3, 4, 5, 6, 7]
    - Step 2: Reverse remaining n-k elements (index k to n-1):
              [3, 4, 5, 6, 7] -> [7, 6, 5, 4, 3], array becomes [2, 1, 7, 6, 5, 4, 3]
    - Step 3: Reverse the entire array (index 0 to n-1):
              [2, 1, 7, 6, 5, 4, 3] -> [3, 4, 5, 6, 7, 1, 2]
              
    Time Complexity: O(N) (k/2 + (n-k)/2 + n/2 = N swaps total)
    Space Complexity: O(1) auxiliary space (in-place)
    """
    n = len(nums)
    if n <= 1:
        return nums

    # Rotating by n brings the array back to itself, so reduce k
    k = k % n
    if k == 0:
        return nums

    # 1. Reverse the first k elements: [0 .. k-1]
    reverse_subarray(nums, 0, k - 1)

    # 2. Reverse the remaining elements: [k .. n-1]
    reverse_subarray(nums, k, n - 1)

    # 3. Reverse the whole array: [0 .. n-1]
    reverse_subarray(nums, 0, n - 1)

    return nums


# Call the function (modifies the array in-place) and display the result
rotated = left_rotate_by_k(array, k)
print(f"Result: Array after left rotation by {k} places: {rotated}")



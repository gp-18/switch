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

# Write your solution below


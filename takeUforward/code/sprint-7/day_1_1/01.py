# Split Array - Largest Sum
# Given an integer array a of size n and an integer k.
# Split the array a into k non-empty subarrays such that the largest sum
# of any subarray is minimized. Return the minimized largest sum of the split.
#
# Example 1:
# Input:  a = [1, 2, 3, 4, 5], k = 3
# Output: 6
# Explanation: Optimal split is [1, 2, 3] | [4] | [5], max sum = 6.
#
# Example 2:
# Input:  a = [3, 5, 1], k = 3
# Output: 5
# Explanation: Split is [3] | [5] | [1], max sum = 5.
#
# Example 3:
# Input:  a = [1, 2, 3, 4, 5], k = 2
# Output: 9
#
# Think About:
# - Search space: low = max(a), high = sum(a).
# - Equivalence to Book Allocation & Painter's Partition problems.
# - Monotonicity: As maxSum increases, required partitions decreases or stays the same.
# - If partitions > k: mid is too small, search right (low = mid + 1).
# - Else: mid is feasible, search left (high = mid - 1) to minimize.
# - Time Complexity: O(N * log(sum(a) - max(a)))
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array (n) : "))
array = []

for i in range(length):
    value = int(input(f"Enter element at index {i} : "))
    array.append(value)

k = int(input("Enter number of subarrays (k) : "))

print(f"Your array : {array} with k = {k}")

# Write your solution below:
# Optimal Approach: Binary Search on Answers [max(a), sum(a)]
# Time Complexity: O(N * log(sum(a) - max(a))) | Space Complexity: O(1)

def count_partitions(a, max_sum):
    partitions = 1
    subarray_sum = 0

    for num in a:
        if subarray_sum + num <= max_sum:
            # Add element to current subarray
            subarray_sum += num
        else:
            # Start a new subarray with current element
            partitions += 1
            subarray_sum = num

    return partitions

low = max(array)
high = sum(array)
ans = high

while low <= high:
    mid = low + (high - low) // 2
    partitions = count_partitions(array, mid)

    if partitions > k:
        # Too many partitions needed, increase allowed max sum
        low = mid + 1
    else:
        ans = mid
        # Feasible within k partitions, try to minimize max sum
        high = mid - 1

print(f"The minimized largest subarray sum is : {ans}")

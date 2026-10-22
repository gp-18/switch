# Count Quadruplets with Sum Less Than Target (4 Sum Smaller)
# Given an integer array nums of length n and an integer target, return the total
# number of unique index quadruplets (a, b, c, d) with 0 <= a < b < c < d < n
# such that nums[a] + nums[b] + nums[c] + nums[d] < target.
#
# Example 1:
# Input:  nums = [1, 2, 3, 4, 5], target = 12
# Output: 2  # Quadruplets: (1, 2, 3, 4) sum=10, (1, 2, 3, 5) sum=11
#
# Example 2:
# Input:  nums = [-2, 0, 1, 3, 5], target = 5
# Output: 4
#
# Example 3 (Edge Case):
# Input:  nums = [2, 3, 4, 5], target = 14
# Output: 0  # Min sum is 14 (not < 14)
#
# Think About:
# - Sort nums in ascending order.
# - count = 0
# - Loop i from 0 to n - 4:
#   * Loop j from i + 1 to n - 3:
#       * Set k = j + 1 and l = n - 1.
#       * While k < l:
#           if nums[i] + nums[j] + nums[k] + nums[l] < target:
#               # Because array is sorted, every element between k+1 and l
#               # paired with nums[i], nums[j], nums[k] will also have sum < target!
#               count += (l - k)
#               k += 1
#           else:
#               l -= 1
# - Time Complexity: O(N^3)
# - Space Complexity: O(1) auxiliary space
#


length = int(input("Enter the length of the array: "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i}: "))
    array.append(value)

target = int(input("Enter the target sum: "))

print(f"Your array has become: {array}, target is: {target}")

n = len(array)
array.sort()

count = 0

for i in range(n - 3):
    for j in range(i + 1, n - 2):
        k = j + 1
        l = n - 1

        while k < l:
            total = array[i] + array[j] + array[k] + array[l]

            if total < target:
                count += l - k
                k += 1
            else:
                l -= 1

print(count)

# 4 Sum
# Given an integer array nums and an integer target, return all unique quadruplets
# [nums[a], nums[b], nums[c], nums[d]] such that:
#   - a, b, c, d are distinct valid indices (0 <= a < b < c < d < n)
#   - nums[a] + nums[b] + nums[c] + nums[d] == target
# The solution set must not contain duplicate quadruplets.
#
# Example 1:
# Input:  nums = [1, -2, 3, 5, 7, 9], target = 7
# Output: [[-2, 1, 3, 5]]
#
# Example 2:
# Input:  nums = [1, 1, 3, 4, -3], target = 5
# Output: [[-3, 1, 3, 4]]
#
# Example 3 (Edge Case):
# Input:  nums = [7, -7, 1, 2, 14, 3], target = 9
# Output: []  # No quadruplets sum to target
#
# Think About:
# - Sort the array first in ascending order.
# - Fix first element with loop i from 0 to n - 4 (skip duplicate nums[i]).
# - Fix second element with loop j from i + 1 to n - 3 (skip duplicate nums[j]).
# - Use two moving pointers k = j + 1 and l = n - 1 for the remaining pair:
#   * If nums[i] + nums[j] + nums[k] + nums[l] == target:
#       record quadruplet, skip duplicate k and l values, move both inward.
#   * If sum < target: advance k += 1 (need a larger sum).
#   * If sum > target: decrement l -= 1 (need a smaller sum).
# - Time Complexity: O(N^3)
# - Space Complexity: O(1) auxiliary space (excluding result list)
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

ans = []

for i in range(n - 3):
    if i > 0 and array[i] == array[i - 1]:
        continue

    for j in range(i + 1, n - 2):
        if j > i + 1 and array[j] == array[j - 1]:
            continue

        k = j + 1
        l = n - 1

        while k < l:
            total = array[i] + array[j] + array[k] + array[l]

            if total == target:
                temp = [array[i], array[j], array[k], array[l]]
                ans.append(temp)

                k += 1
                l -= 1

                while k < l and array[k] == array[k - 1]:
                    k += 1

                while k < l and array[l] == array[l + 1]:
                    l -= 1

            elif total < target:
                k += 1
            else:
                l -= 1

print(ans)
                
        
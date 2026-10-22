# Check if Quadruplet with Target Sum Exists
# Given an integer array nums and an integer target, determine whether there exists any
# quadruplet (nums[a], nums[b], nums[c], nums[d]) with distinct indices a < b < c < d
# such that their sum equals target. Return True if such a quadruplet exists, otherwise False.
#
# Example 1:
# Input:  nums = [1, 0, -1, 0, -2, 2], target = 0
# Output: True  # Quadruplet (-2, -1, 1, 2) sums to 0
#
# Example 2:
# Input:  nums = [1, 2, 3, 4], target = 50
# Output: False # Max sum is 1 + 2 + 3 + 4 = 10 != 50
#
# Example 3 (Edge Case):
# Input:  nums = [1, 2, 3], target = 6
# Output: False # Array length < 4
#
# Think About:
# - Sort nums in ascending order.
# - Loop i from 0 to n - 4 (fix first number).
# - Loop j from i + 1 to n - 3 (fix second number).
# - Use two moving pointers: k = j + 1 and l = n - 1.
# - While k < l:
#   * current_sum = nums[i] + nums[j] + nums[k] + nums[l]
#   * If current_sum == target: return True immediately.
#   * Else if current_sum < target: k += 1
#   * Else: l -= 1
# - If all loops finish without match, return False.
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

array.sort()
n = len(array)
found = False

for i in range(n - 3):
    for j in range(i + 1, n - 2):
        k = j + 1
        l = n - 1

        while k < l:
            total = array[i] + array[j] + array[k] + array[l]

            if total == target:
                found = True
                break
            elif total < target:
                k += 1
            else:
                l -= 1

        if found:
            break

    if found:
        break

print(found)

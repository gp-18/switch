# Find Any One Quadruplet Equal to Target
# Given an integer array nums and an integer target, find and return any one
# quadruplet [nums[a], nums[b], nums[c], nums[d]] with distinct indices such that
# their sum equals target. If no such quadruplet exists, return an empty list [].
#
# Example 1:
# Input:  nums = [2, 7, 4, 0, 9, 5, 1, 3], target = 20
# Output: [2, 4, 5, 9]  # 2 + 4 + 5 + 9 = 20
#
# Example 2:
# Input:  nums = [1, 2, 3, 4, 5], target = 100
# Output: []
#
# Example 3 (Edge Case):
# Input:  nums = [5, 5, 5, 5], target = 20
# Output: [5, 5, 5, 5]  # Exact size 4 array
#
# Think About:
# - Sort nums in ascending order.
# - Loop i from 0 to n - 4:
#   * Loop j from i + 1 to n - 3:
#       * Set k = j + 1 and l = n - 1.
#       * While k < l:
#           total = nums[i] + nums[j] + nums[k] + nums[l]
#           if total == target: return [nums[i], nums[j], nums[k], nums[l]]
#           elif total < target: k += 1
#           else: l -= 1
# - Return [] if no match found.
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

ans = []

for i in range(n - 3):
    for j in range(i + 1, n - 2):
        k = j + 1
        l = n - 1

        while k < l:
            total = array[i] + array[j] + array[k] + array[l]

            if total == target:
                ans = [array[i], array[j], array[k], array[l]]
                break
            elif total < target:
                k += 1
            else:
                l -= 1

        if ans:
            break

    if ans:
        break

print(ans)

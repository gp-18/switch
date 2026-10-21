# 4 Sum Closest to Target (Amazon, Microsoft, Bloomberg)
# Given an integer array nums of length n and an integer target, find four integers in
# nums such that their sum is closest to target. Return the sum of the four integers.
# Assume exactly one closest sum exists.
#
# Example 1:
# Input:  nums = [1, 0, -1, 0, -2, 2], target = 1
# Output: 1  # Quadruplet (-2, 0, 1, 2) has sum = 1, exact match
#
# Example 2:
# Input:  nums = [-1, 2, 1, -4, 5, -3], target = 5
# Output: 4  # Closest sum is 4
#
# Example 3 (Edge Case):
# Input:  nums = [1, 1, 1, 1], target = -100
# Output: 4  # Small array far from negative target
#
# Think About:
# - Sort nums in ascending order.
# - Initialize closest_sum = nums[0] + nums[1] + nums[2] + nums[3].
# - Loop i from 0 to n - 4:
#   * Loop j from i + 1 to n - 3:
#       * Set k = j + 1 and l = n - 1.
#       * While k < l:
#           current_sum = nums[i] + nums[j] + nums[k] + nums[l]
#           if abs(current_sum - target) < abs(closest_sum - target):
#               closest_sum = current_sum
#           if current_sum == target:
#               return target
#           elif current_sum < target:
#               k += 1
#           else:
#               l -= 1
# - Return closest_sum.
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

if n < 4:
    print("At least 4 elements are required.")
else:
    closest_sum = array[0] + array[1] + array[2] + array[3]
    is_found = False

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            k = j + 1
            l = n - 1

            while k < l:
                current_sum = (
                    array[i] + array[j] + array[k] + array[l]
                )

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum == target:
                    closest_sum = target
                    is_found = True
                    break
                elif current_sum < target:
                    k += 1
                else:
                    l -= 1

            if is_found:
                break

        if is_found:
            break

    print(f"Closest sum to target {target} is {closest_sum}")

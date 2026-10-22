# Check if Triplet with Zero Sum Exists
# Given an integer array nums, determine whether there exists any triplet
# (nums[i], nums[j], nums[k]) with i != j != k such that their sum equals 0.
# Return True if such a triplet exists, otherwise return False.
#
# Example 1:
# Input:  nums = [0, -1, 2, -3, 1]
# Output: True  # Triplet (0, -1, 1) or (-3, 1, 2) sums to 0
#
# Example 2:
# Input:  nums = [1, 2, 3]
# Output: False # Smallest sum is 1 + 2 + 3 = 6 != 0
#
# Example 3 (Edge Case):
# Input:  nums = [1, -1]
# Output: False  # Length < 3
#
# Think About:
# - Sort the array first.
# - Loop i from 0 to n - 3, pin nums[i].
# - Set low = i + 1, high = n - 1.
# - While low < high:
#   * If nums[i] + nums[low] + nums[high] == 0: return True!
#   * If sum < 0: low += 1 (need a bigger sum).
#   * If sum > 0: high -= 1 (need a smaller sum).
# - If the loop finishes without finding any triplet, return False.
# - Time Complexity: O(N^2)
# - Space Complexity: O(1) auxiliary space
#


length = int(input("Enter the length of the array: "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i}: "))
    array.append(value)

print(f"Your array has become: {array} and now doing the operations on it.")

array.sort()
n = len(array)
found = False

for i in range(n - 2):
    low = i + 1
    high = n - 1

    while low < high:
        current_sum = array[i] + array[low] + array[high]

        if current_sum == 0:
            found = True
            break
        elif current_sum < 0:
            low += 1
        else:
            high -= 1

    if found:
        break

print(found)

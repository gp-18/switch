# Union of Two Sorted Arrays
# Given two sorted integer arrays a and b, return a sorted list containing the union of elements
# from both arrays (all unique elements appearing in either array, with no duplicates in the output).
#
# Example 1:
# Input:  a = [1, 2, 3, 4], b = [2, 3, 5]
# Output: [1, 2, 3, 4, 5]
#
# Example 2:
# Input:  a = [2, 2, 3], b = [1, 1, 2]
# Output: [1, 2, 3]
#
# Example 3 (Edge Case):
# Input:  a = [1, 1, 1], b = [1, 1]
# Output: [1]  # Duplicates collapsed into one
#
# Think About:
# - Put i = 0 on a and j = 0 on b, with empty list result = [].
# - Helper rule: only append val if len(result) == 0 or result[-1] != val.
# - While i < len(a) and j < len(b):
#   * If a[i] <= b[j]: add a[i] via helper rule, i += 1.
#   * Else: add b[j] via helper rule, j += 1.
# - Drain remaining elements from a or b using helper rule.
# - Time Complexity: O(N + M)
# - Space Complexity: O(N + M) for output
#

len1 = int(input("Enter the length of the first sorted array : "))
array1 = []
for i in range(len1):
    value = int(input(f"Enter the value to insert at index {i} for array 1 : "))
    array1.append(value)

len2 = int(input("Enter the length of the second sorted array : "))
array2 = []
for i in range(len2):
    value = int(input(f"Enter the value to insert at index {i} for array 2 : "))
    array2.append(value)

print(f"Array 1 : {array1}")
print(f"Array 2 : {array2} and now doing the operations on them.")

# Write your solution below


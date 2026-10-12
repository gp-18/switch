# Intersection of Two Sorted Arrays
# Given two sorted integer arrays a and b, return a list of elements that appear in both arrays
# (including duplicates if an element appears multiple times in both).
#
# Example 1:
# Input:  a = [1, 2, 2, 3, 4], b = [2, 2, 4, 6]
# Output: [2, 2, 4]
#
# Example 2:
# Input:  a = [1, 3, 5], b = [2, 4, 6]
# Output: []
#
# Example 3 (Edge Case):
# Input:  a = [3, 3, 3], b = [3, 3]
# Output: [3, 3]  # Min frequency of common element is preserved
#
# Think About:
# - Put i = 0 on a and j = 0 on b.
# - While i < len(a) and j < len(b):
#   * If a[i] < b[j]: move i += 1.
#   * If b[j] < a[i]: move j += 1.
#   * If a[i] == b[j]: common element! Append to result, then i += 1, j += 1.
# - Time Complexity: O(N + M)
# - Space Complexity: O(min(N, M)) for output
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


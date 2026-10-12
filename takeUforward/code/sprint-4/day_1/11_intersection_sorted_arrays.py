# Intersection of Two Sorted Arrays
# Given two sorted arrays a and b, find and return the intersection of the two arrays
# (elements common to both arrays).
#
# Example 1:
# Input:  a = [1, 2, 2, 3, 3, 4, 5, 6], b = [2, 3, 3, 5, 6, 6, 7]
# Output: [2, 3, 3, 5, 6]
#
# Example 2:
# Input:  a = [1, 2, 3], b = [4, 5, 6]
# Output: []
#
# Think About:
# - Two pointers i = 0 and j = 0:
#   * If a[i] < b[j]: increment i += 1.
#   * If b[j] < a[i]: increment j += 1.
#   * If a[i] == b[j]: common element found! Append a[i] to intersection, then increment both i += 1 and j += 1.
# - Stop when either pointer reaches the end of its array.
# - Time Complexity: O(N + M)
# - Space Complexity: O(1) auxiliary space (excluding output array).
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


# Union of Two Sorted Arrays
# Given two sorted arrays a and b, return a sorted list containing the union of elements from both arrays
# (all unique elements present in either array).
#
# Example 1:
# Input:  a = [1, 2, 3, 4, 5], b = [2, 3, 4, 4, 5, 6]
# Output: [1, 2, 3, 4, 5, 6]
#
# Example 2:
# Input:  a = [2, 2, 3, 4, 5], b = [1, 1, 2, 3, 4]
# Output: [1, 2, 3, 4, 5]
#
# Think About:
# - Two-pointer traversal: i = 0 for a and j = 0 for b.
# - Compare a[i] and b[j]:
#   * If a[i] <= b[j]: consider a[i] for insertion; increment i += 1.
#   * Else: consider b[j] for insertion; increment j += 1.
# - Only append an element if the union list is empty or union[-1] != element (prevents duplicates).
# - Exhaust remaining elements in a or b with the same duplicate check.
# - Time Complexity: O(N + M)
# - Space Complexity: O(N + M) for the output array.
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


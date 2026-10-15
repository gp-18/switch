# Merge Two Sorted Arrays
# Given two sorted integer arrays a and b, merge them into a single new sorted array
# containing all elements from both.
#
# Example 1:
# Input:  a = [1, 3, 5], b = [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]
#
# Example 2:
# Input:  a = [1, 2, 7], b = [3, 4]
# Output: [1, 2, 3, 4, 7]
#
# Example 3 (Edge Case):
# Input:  a = [], b = [1, 5, 9]
# Output: [1, 5, 9]  # One array is empty
#
# Think About:
# - Put finger i = 0 on array a and j = 0 on array b.
# - Compare a[i] and b[j]:
#   * If a[i] <= b[j]: append a[i] to result and i += 1.
#   * Else: append b[j] to result and j += 1.
# - Append all leftover elements from the other array when one runs out.
# - Time Complexity: O(N + M)
# - Space Complexity: O(N + M) for output list
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

i = 0
j = 0
merged = []

while i < len(array1) and j < len(array2):
    if array1[i] <= array2[j]:
        merged.append(array1[i])
        i += 1
    else:
        merged.append(array2[j])
        j += 1

while i < len(array1):
    merged.append(array1[i])
    i += 1

while j < len(array2):
    merged.append(array2[j])
    j += 1

print("Merged array :", merged)

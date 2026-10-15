# Check if Array A is a Subsequence of Array B
# Given two integer arrays a and b, return True if a is a subsequence of b, or False otherwise.
# (An array a is a subsequence of b if a can be formed by deleting zero or more elements from b
# without changing the order of the remaining elements).
#
# Example 1:
# Input:  a = [1, 3, 5], b = [1, 2, 3, 4, 5, 6]
# Output: True  # 1, 3, 5 appear in b in the exact same relative order
#
# Example 2:
# Input:  a = [5, 3], b = [1, 2, 3, 4, 5]
# Output: False  # Elements are present, but their order is reversed
#
# Example 3 (Edge Case):
# Input:  a = [], b = [1, 2, 3]
# Output: True  # Empty array is always a valid subsequence
#
# Think About:
# - Put finger i = 0 on a (target pattern) and j = 0 on b (main list).
# - While i < len(a) and j < len(b):
#   * If a[i] == b[j]: matched current number! Advance i += 1.
#   * Always advance j += 1 to keep searching forward in b.
# - If i == len(a), all elements were matched in order: return True, otherwise False.
# - Time Complexity: O(len(b))
# - Space Complexity: O(1) auxiliary space
#

len_a = int(input("Enter the length of array a (candidate subsequence) : "))
array_a = []
for i in range(len_a):
    value = int(input(f"Enter the value to insert at index {i} for array a : "))
    array_a.append(value)

len_b = int(input("Enter the length of array b (main array) : "))
array_b = []
for i in range(len_b):
    value = int(input(f"Enter the value to insert at index {i} for array b : "))
    array_b.append(value)

print(f"Array a : {array_a}")
print(f"Array b : {array_b} and now doing the operations on them.")

# Write your solution below

i = 0
j = 0

while i < len(array_a) and j < len(array_b):
    if array_a[i] == array_b[j]:
        i += 1
    j += 1

if i == len(array_a):
    print(True)
else:
    print(False)

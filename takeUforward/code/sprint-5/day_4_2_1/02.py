# Intersection of Two Sorted Arrays
# Given two sorted integer arrays nums1 and nums2, return an array containing their
# intersection (distinct common elements present in both arrays).
# The returned array must be sorted in ascending order.
#
# Example 1:
# Input:  nums1 = [1, 2, 2, 3, 4], nums2 = [2, 2, 3, 5]
# Output: [2, 3]
# Explanation: 2 and 3 are present in both arrays. Only distinct values are included.
#
# Example 2:
# Input:  nums1 = [1, 3, 5, 7], nums2 = [2, 4, 6, 8]
# Output: []
# Explanation: No common elements.
#
# Example 3:
# Input:  nums1 = [2, 2, 2], nums2 = [2, 2]
# Output: [2]
#
# Think About:
# - Two pointers i = 0, j = 0.
# - If nums1[i] < nums2[j]: i += 1 (nums1[i] is too small to match).
# - If nums1[i] > nums2[j]: j += 1 (nums2[j] is too small to match).
# - If nums1[i] == nums2[j]:
#     Append to result if result is empty or result[-1] != nums1[i] (deduplication).
#     Advance both pointers: i += 1, j += 1.
# - Time Complexity: O(m + n)
# - Space Complexity: O(1) auxiliary space (excluding result array)
#

m = int(input("Enter length of sorted nums1 : "))
nums1 = []
for i in range(m):
    value = int(input(f"Enter element {i} of nums1 : "))
    nums1.append(value)

n = int(input("Enter length of sorted nums2 : "))
nums2 = []
for i in range(n):
    value = int(input(f"Enter element {i} of nums2 : "))
    nums2.append(value)

print(f"nums1: {nums1}")
print(f"nums2: {nums2}")
print("Finding intersection of sorted arrays...")

# Write your solution below:


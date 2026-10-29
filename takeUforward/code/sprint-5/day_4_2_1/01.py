# Merge Two Sorted Arrays (Forward Two Pointers)
# Given two sorted integer arrays nums1 of size m and nums2 of size n,
# merge them into a single sorted array and return it.
#
# Example 1:
# Input:  nums1 = [1, 3, 5, 7], nums2 = [2, 4, 6, 8]
# Output: [1, 2, 3, 4, 5, 6, 7, 8]
#
# Example 2:
# Input:  nums1 = [5, 10, 15], nums2 = [2, 3, 20]
# Output: [2, 3, 5, 10, 15, 20]
#
# Example 3:
# Input:  nums1 = [1, 2], nums2 = []
# Output: [1, 2]
#
# Think About:
# - Initialize i = 0, j = 0, and merged = []
# - While i < len(nums1) and j < len(nums2):
#     Compare nums1[i] and nums2[j], append the smaller element, and advance that pointer.
# - After loop, append any remaining elements from nums1 and nums2.
# - Time Complexity: O(m + n)
# - Space Complexity: O(m + n) for the merged array
#

m = int(input("Enter length of nums1 : "))
nums1 = []
for i in range(m):
    value = int(input(f"Enter element {i} of nums1 : "))
    nums1.append(value)

n = int(input("Enter length of nums2 : "))
nums2 = []
for i in range(n):
    value = int(input(f"Enter element {i} of nums2 : "))
    nums2.append(value)

print(f"nums1: {nums1}")
print(f"nums2: {nums2}")
print("Performing merge operation...")

# Write your solution below:


# Merge Two Sorted Arrays Without Extra Space
# Given two integer arrays nums1 and nums2, both sorted in non-decreasing order.
# nums1 has length m + n, where the first m elements are valid and rest are 0s.
# nums2 has length n.
# Merge nums2 into nums1 in-place in non-decreasing order.
#
# Example 1:
# Input:  nums1 = [-5, -2, 4, 5, 0, 0, 0], m = 4, nums2 = [-3, 1, 8], n = 3
# Output: [-5, -3, -2, 1, 4, 5, 8]
#
# Example 2:
# Input:  nums1 = [0, 2, 7, 8, 0, 0, 0], m = 4, nums2 = [-7, -3, -1], n = 3
# Output: [-7, -3, -1, 0, 2, 7, 8]
#
# Example 3:
# Input:  nums1 = [1, 3, 5, 0, 0, 0, 0], m = 3, nums2 = [2, 4, 6, 7], n = 4
# Output: [1, 2, 3, 4, 5, 6, 7]
#
# Think About:
# - Merging from the front requires O(m * n) shifting or extra space.
# - Merging from the back (three pointers: i = m - 1, j = n - 1, k = m + n - 1)
#   places the largest elements into the empty/zero buffer slots without overwriting
#   uninspected elements in nums1.
# - If j >= 0 remains after i < 0, copy remaining elements of nums2 into nums1.
# - Time Complexity: O(m + n)
# - Space Complexity: O(1) auxiliary space (in-place)
#

m = int(input("Enter the number of valid elements in nums1 (m) : "))
nums1 = []

for i in range(m):
    value = int(input(f"Enter element {i} of nums1 : "))
    nums1.append(value)

n = int(input("Enter the number of elements in nums2 (n) : "))
nums2 = []

for i in range(n):
    value = int(input(f"Enter element {i} of nums2 : "))
    nums2.append(value)

# Append n buffer zeros to nums1 so it has length m + n
nums1.extend([0] * n)

print(f"Initial nums1 (with buffer) : {nums1}")
print(f"Initial nums2 : {nums2}")
print("Performing in-place reverse three-pointer merge...")

# Write your solution below:
# Three pointers:
# i -> points to the last valid element in nums1
# j -> points to the last element in nums2
# k -> points to the last position in nums1 (write index)
i = m - 1
j = n - 1
k = m + n - 1

while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1

# If elements remain in nums2, copy them over
# (If elements remain in nums1, they are already in their correct places)
while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1

print(f"Final merged array nums1 : {nums1}")

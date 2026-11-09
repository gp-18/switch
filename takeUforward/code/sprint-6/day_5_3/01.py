# Median of 2 Sorted Arrays
# Given two sorted arrays arr1 and arr2 of size m and n respectively,
# return the median of the two sorted arrays.
#
# Example 1:
# Input:  arr1 = [2, 4, 6], arr2 = [1, 3, 5]
# Output: 3.5
# Explanation: Combined array [1, 2, 3, 4, 5, 6]. Median = (3 + 4) / 2 = 3.5.
#
# Example 2:
# Input:  arr1 = [2, 4, 6], arr2 = [1, 3]
# Output: 3.0
# Explanation: Combined array [1, 2, 3, 4, 6]. Median = 3.0.
#
# Example 3:
# Input:  arr1 = [2, 4, 5], arr2 = [1, 6]
# Output: 4.0
#
# Think About:
# - Ensure arr1 is the smaller array to minimize binary search range: O(log(min(m, n))).
# - Partition merged array into two halves of size left = (m + n + 1) // 2.
# - Partition condition: l1 <= r2 and l2 <= r1.
# - If l1 > r2: search left (high = mid1 - 1).
# - If l2 > r1: search right (low = mid1 + 1).
# - If odd total length: median = max(l1, l2).
# - If even total length: median = (max(l1, l2) + min(r1, r2)) / 2.0.
# - Time Complexity: O(log(min(m, n)))
# - Space Complexity: O(1) auxiliary space
#

length1 = int(input("Enter size of first sorted array (m) : "))
array1 = []
for i in range(length1):
    value = int(input(f"Enter element at index {i} for array 1 : "))
    array1.append(value)

length2 = int(input("Enter size of second sorted array (n) : "))
array2 = []
for i in range(length2):
    value = int(input(f"Enter element at index {i} for array 2 : "))
    array2.append(value)

print(f"Array 1 : {array1}")
print(f"Array 2 : {array2}")

# Write your solution below:
# Optimal Approach: Binary Search on Partition of Smaller Array
# Time Complexity: O(log(min(m, n))) | Space Complexity: O(1)

def find_median_sorted_arrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    # Ensure arr1 is the smaller array
    if n1 > n2:
        return find_median_sorted_arrays(arr2, arr1)

    total_len = n1 + n2
    left_half_size = (n1 + n2 + 1) // 2

    low = 0
    high = n1

    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left_half_size - mid1

        # Border elements around the partition cut
        l1 = arr1[mid1 - 1] if mid1 > 0 else float('-inf')
        r1 = arr1[mid1] if mid1 < n1 else float('inf')
        l2 = arr2[mid2 - 1] if mid2 > 0 else float('-inf')
        r2 = arr2[mid2] if mid2 < n2 else float('inf')

        # Check if the partition is valid
        if l1 <= r2 and l2 <= r1:
            if total_len % 2 == 1:
                return float(max(l1, l2))
            else:
                return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            # Too many elements taken from arr1, move left
            high = mid1 - 1
        else:
            # Too few elements taken from arr1, move right
            low = mid1 + 1

    return 0.0

ans = find_median_sorted_arrays(array1, array2)

print(f"The median of the two sorted arrays is : {ans}")


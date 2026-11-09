# Kth Element of 2 Sorted Arrays
# Given two sorted arrays a and b of size m and n respectively,
# find the kth element of the final sorted array.
#
# Example 1:
# Input:  a = [2, 3, 6, 7, 9], b = [1, 4, 8, 10], k = 5
# Output: 6
# Explanation: Final merged array: [1, 2, 3, 4, 6, 7, 8, 9, 10]. 5th element is 6.
#
# Example 2:
# Input:  a = [100, 112, 256, 349, 770], b = [72, 86, 113, 119, 265, 445, 892], k = 7
# Output: 256
#
# Example 3:
# Input:  a = [2, 3, 6], b = [7, 9], k = 4
# Output: 7
#
# Think About:
# - Similar to median of 2 sorted arrays, partition combined array to form left half of size k.
# - Ensure array a is the smaller array: len(a) <= len(b).
# - Search range for elements taken from a:
#   * low = max(0, k - n) (even if all n elements of b are taken, need k - n from a)
#   * high = min(k, m) (cannot take more than m or more than k from a)
# - If l1 <= r2 and l2 <= r1: partition is valid, answer is max(l1, l2).
# - If l1 > r2: search left (high = mid1 - 1).
# - Else: search right (low = mid1 + 1).
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

k = int(input("Enter k : "))

print(f"Array 1 : {array1}")
print(f"Array 2 : {array2}")
print(f"k = {k}")

# Write your solution below:
# Optimal Approach: Binary Search on Partition of Smaller Array
# Time Complexity: O(log(min(m, n))) | Space Complexity: O(1)

def find_kth_element(a, b, target_k):
    m = len(a)
    n = len(b)

    # Ensure a is the smaller array
    if m > n:
        return find_kth_element(b, a, target_k)

    # Search range bounds
    low = max(0, target_k - n)
    high = min(target_k, m)

    while low <= high:
        mid1 = (low + high) // 2
        mid2 = target_k - mid1

        # Border elements around the partition cut
        l1 = a[mid1 - 1] if mid1 > 0 else float('-inf')
        r1 = a[mid1] if mid1 < m else float('inf')
        l2 = b[mid2 - 1] if mid2 > 0 else float('-inf')
        r2 = b[mid2] if mid2 < n else float('inf')

        # Check if the partition is valid
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            # Too many elements taken from a, search left
            high = mid1 - 1
        else:
            # Too few elements taken from a, search right
            low = mid1 + 1

    return -1

ans = find_kth_element(array1, array2, k)

print(f"The {k}-th element of the two sorted arrays is : {ans}")


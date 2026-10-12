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

def find_intersection(a, b):
    """
    Find the intersection of two sorted arrays a and b.
    Returns a list containing all elements that appear in both arrays.
    
    Two-Pointer Technique:
    - Pointer `i` starts at 0 for array `a`.
    - Pointer `j` starts at 0 for array `b`.
    - Because both arrays are sorted:
      * If a[i] < b[j]: The element a[i] is too small to match b[j], and since `b` is sorted,
        no future element in `b` will match a[i]. So advance `i += 1`.
      * If b[j] < a[i]: The element b[j] is too small to match a[i]. Advance `j += 1`.
      * If a[i] == b[j]: We have found a common element! Append to intersection,
        and advance both `i += 1` and `j += 1`.
    - Terminate as soon as either pointer runs off the end of its array.
    
    Time Complexity: O(N + M) (each step advances at least one pointer)
    Space Complexity: O(1) auxiliary space (excluding the output list)
    """
    n, m = len(a), len(b)
    i, j = 0, 0
    intersection_list = []

    # Traverse while both pointers are within bounds
    while i < n and j < m:
        if a[i] < b[j]:
            # a[i] is smaller, advance i to find a possible match
            i += 1
        elif b[j] < a[i]:
            # b[j] is smaller, advance j to find a possible match
            j += 1
        else:
            # a[i] == b[j], common element found!
            intersection_list.append(a[i])
            # Move both pointers past the matched element
            i += 1
            j += 1

    return intersection_list


# Call the function and display the result
intersection_result = find_intersection(array1, array2)
print(f"Result: Intersection of the two sorted arrays: {intersection_result}")



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

def find_union(a, b):
    """
    Find the union of two sorted arrays a and b.
    Returns a sorted list containing all distinct elements from both arrays.
    
    Two-Pointer Approach:
    - Pointer `i` tracks array `a`, pointer `j` tracks array `b`.
    - In each iteration:
      * Compare a[i] and b[j].
      * Take the smaller (or equal) value as the candidate to append.
      * Before appending, check `if not union_list or union_list[-1] != candidate`:
        this ensures that repeated elements (even within the same array) are not added twice.
      * Move the pointer of the chosen element forward.
    - When one array finishes, exhaust the remainder of the other array with the same duplicate check.
    
    Time Complexity: O(N + M) (each element in both arrays is visited once)
    Space Complexity: O(N + M) (to store the returned union list)
    """
    n, m = len(a), len(b)
    i, j = 0, 0
    union_list = []

    # Helper function to avoid duplicate elements in the union
    def add_if_unique(element):
        if not union_list or union_list[-1] != element:
            union_list.append(element)

    # Step 1: Compare elements from both arrays and add the smaller one
    while i < n and j < m:
        if a[i] <= b[j]:
            add_if_unique(a[i])
            i += 1
        else:
            add_if_unique(b[j])
            j += 1

    # Step 2: Append remaining elements of array a (if any)
    while i < n:
        add_if_unique(a[i])
        i += 1

    # Step 3: Append remaining elements of array b (if any)
    while j < m:
        add_if_unique(b[j])
        j += 1

    return union_list


# Call the function and display the result
union_result = find_union(array1, array2)
print(f"Result: Union of the two sorted arrays: {union_result}")



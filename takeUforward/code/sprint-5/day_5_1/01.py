# Longest Consecutive Sequence in an Array
# Given an unsorted integer array nums. Return the length of the longest sequence
# of consecutive integers. The integers can appear in any order.
#
# Example 1:
# Input:  nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: Consecutive sequence is [1, 2, 3, 4], length = 4.
#
# Example 2:
# Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9
# Explanation: Consecutive sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8], length = 9.
#
# Example 3:
# Input:  nums = [1, 9, 3, 10, 4, 20, 2]
# Output: 4
# Explanation: Longest consecutive sequence is [1, 2, 3, 4], length = 4.
#
# Think About:
# - Brute Force: Searching for x+1, x+2 for each element takes O(N^2) or O(N^3).
# - Sorting: Sorting takes O(N log N) time, which violates the O(N) constraint.
# - Optimal Approach: HashSet with Sequence Starting Points:
#   * Insert all elements into a hash set for O(1) average lookup.
#   * An element 'it' is a sequence starting point ONLY if 'it - 1' is NOT in the set.
#   * If 'it - 1' is in the set, skip it (it will be covered from its true starting point).
#   * For starting points, count consecutive elements: while x + 1 in set: x += 1, cnt += 1.
#   * Each element is visited at most twice across the entire run.
# - Time Complexity: O(N) average time
# - Space Complexity: O(N) auxiliary space for the hash set
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below:

# Handle edge case for empty array
if length == 0:
    print("The longest consecutive sequence length is : 0")
else:
    # Insert all elements into set for O(1) lookups and deduplication
    st = set(array)
    longest = 1

    # Traverse unique numbers in the set
    for it in st:
        # Check if 'it' is the starting point of a sequence
        if it - 1 not in st:
            cnt = 1
            x = it

            # Count consecutive elements
            while x + 1 in st:
                x += 1
                cnt += 1

            # Update maximum length found
            longest = max(longest, cnt)

    print(f"The longest consecutive sequence length is : {longest}")

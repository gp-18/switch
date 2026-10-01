# Find the second-largest distinct number in a list; handle duplicates and lists with too few distinct values.

# Example 1:
# Input: [10, 20, 4, 45, 99, 99]
# Output: 45

# Example 2:
# Input: [5, 5, 5]
# Output: None (or "No second distinct largest element")

def find_second_largest(lst):
    distinct_elements = list(set(lst))
    if len(distinct_elements) < 2:
        return None
    distinct_elements.sort(reverse=True)
    return distinct_elements[1]

# Example 1:
print(find_second_largest([10, 20, 4, 45, 99, 99]))

# Example 2:
res = find_second_largest([5, 5, 5])
print(res if res is not None else "No second distinct largest element")

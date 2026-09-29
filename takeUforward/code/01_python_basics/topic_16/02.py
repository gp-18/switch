# Count occurrences of a target in a list without using list.count().

# Example 1:
# Input: lst = [1, 2, 2, 3, 2, 4], target = 2
# Output: 3

# Example 2:
# Input: lst = [1, 2, 3], target = 5
# Output: 0

def count_target(lst, target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count

lst1 = [1, 2, 2, 3, 2, 4]
print(count_target(lst1, 2))

lst2 = [1, 2, 3]
print(count_target(lst2, 5))

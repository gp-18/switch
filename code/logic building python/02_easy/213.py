# Move all elements of a given type to the end of a list.
# Example 1: Input: lst=[1, 0, 2, 0, 3], val=0 -> Output: [1, 2, 3, 0, 0]
# Example 2: Input: lst=['a', 'x', 'b', 'x'], val='x' -> Output: ['a', 'b', 'x', 'x']

lst = [1, 0, 2, 0, 3, 0, 4]
target = 0

non_target = [x for x in lst if x != target]
target_count = lst.count(target)
result = non_target + [target] * target_count

print("Original list:", lst)
print(f"List after moving {target} to end:", result)

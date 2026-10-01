# Find the first occurrence of a target in a list using a loop and break.

# Example 1:
# Input: lst = [10, 20, 30, 40, 20], target = 20
# Output: Found target 20 at index 1

# Example 2:
# Input: lst = [1, 2, 3], target = 5
# Output: Target 5 not found in list

raw_input = input("Enter list elements separated by spaces: ")
lst = raw_input.split()
target = input("Enter target to find: ")

found_index = -1
for index, item in enumerate(lst):
    if item == target:
        found_index = index
        break

if found_index != -1:
    print(f"Found target {target} at index {found_index}")
else:
    print(f"Target {target} not found in list")

# Search a list using for-else; print "not found" only if no break occurs.

# Example 1:
# Input: lst = [4, 7, 9], target = 7
# Output: Found: 7

# Example 2:
# Input: lst = [4, 7, 9], target = 10
# Output: Target 10 not found

raw_input = input("Enter list elements separated by spaces: ")
lst = raw_input.split()
target = input("Enter target to search: ")

for item in lst:
    if item == target:
        print(f"Found: {target}")
        break
else:
    print(f"Target {target} not found")

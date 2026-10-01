# Find whether a target exists in a list and return a Boolean result rather than printing from the search function.

# Example 1:
# Input: lst = [10, 20, 30], target = 20
# Output: True

# Example 2:
# Input: lst = [10, 20, 30], target = 50
# Output: False

def target_exists(lst, target):
    for item in lst:
        if item == target:
            return True
    return False

lst = [10, 20, 30]
print(target_exists(lst, 20))
print(target_exists(lst, 50))

# Write a function with *args that returns the sum of any number of numeric arguments.

# Example 1:
# Input: sum_all(1, 2, 3, 4)
# Output: 10

# Example 2:
# Input: sum_all(5, 10, 15, 20, 25)
# Output: 75

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4))
print(sum_all(5, 10, 15, 20, 25))

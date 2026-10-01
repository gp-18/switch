# Write a function that accepts a list of numbers and returns the sum without printing inside the function.

# Example 1:
# Input: sum_list([1, 2, 3, 4, 5])
# Output: 15

# Example 2:
# Input: sum_list([])
# Output: 0

def sum_list(numbers: list) -> float:
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_list([1, 2, 3, 4, 5]))
print(sum_list([]))

# Given a list of numbers, build a new list containing only even numbers.

# Example 1:
# Input: [1, 2, 3, 4, 5, 6]
# Output: [2, 4, 6]

# Example 2:
# Input: [1, 3, 5]
# Output: []

def get_even_numbers(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens

print(get_even_numbers([1, 2, 3, 4, 5, 6]))
print(get_even_numbers([1, 3, 5]))

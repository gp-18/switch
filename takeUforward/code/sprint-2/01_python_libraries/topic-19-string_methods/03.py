# Split a comma-separated string and clean each item.

# Example 1:
# Input: s = "apple,  banana  , cherry "
# Output: ['apple', 'banana', 'cherry']

# Example 2:
# Input: s = "10, 20 , 30"
# Output: ['10', '20', '30']

s = "apple,  banana  , cherry "
cleaned = [x.strip() for x in s.split(',')]
print(cleaned)

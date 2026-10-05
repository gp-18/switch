# Given two lists of names and scores, combine them using zip() and print each pair.

# Example 1:
# Input: names = ["Alice", "Bob"], scores = [85, 92]
# Output: [('Alice', 85), ('Bob', 92)]

# Example 2:
# Input: names = ["Raj", "Simran"], scores = [90, 95]
# Output: [('Raj', 90), ('Simran', 95)]

names = ["Alice", "Bob"]
scores = [85, 92]
pairs = list(zip(names, scores))
print(pairs)

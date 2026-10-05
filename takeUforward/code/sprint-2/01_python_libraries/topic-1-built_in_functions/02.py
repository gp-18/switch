# Sort a list of strings by length from shortest to longest.

# Example 1:
# Input: words = ["apple", "pie", "banana", "kiwi"]
# Output: ['pie', 'kiwi', 'apple', 'banana']

# Example 2:
# Input: words = ["programming", "code", "python"]
# Output: ['code', 'python', 'programming']

words = ["apple", "pie", "banana", "kiwi"]
sorted_words = sorted(words, key=len)
print(sorted_words)

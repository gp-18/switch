# Sort a list of strings from shortest to longest.
# Example 1: Input: ['apple', 'cat', 'banana', 'hi'] -> Output: ['hi', 'cat', 'apple', 'banana']
# Example 2: Input: ['python', 'c', 'java'] -> Output: ['c', 'java', 'python']

words = ["apple", "cat", "banana", "hi"]

sorted_words = sorted(words, key=len)
print("Original words:", words)
print("Sorted by length:", sorted_words)

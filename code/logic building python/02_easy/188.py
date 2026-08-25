# Split and join a string.
# Example 1: Input: 'hello world python' -> Output: hello-world-python
# Example 2: Input: 'a b c' -> Output: a-b-c

text = input("Enter a string: ")

# Split string into words
words = text.split(" ")

# Join words with a hyphen '-'
joined_text = "-".join(words)

print("Split list:", words)
print("Joined string:", joined_text)

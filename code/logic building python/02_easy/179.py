# Remove punctuation from a string.
# Example 1: Input: 'Hello, World!' -> Output: Hello World
# Example 2: Input: 'Python 3.10!' -> Output: Python 310

import string

text = input("Enter a string: ")

no_punct = ""
for char in text:
    if char not in string.punctuation:
        no_punct += char

print("String without punctuation:", no_punct)

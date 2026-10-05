# Remove punctuation from a sentence using a character set from string.

# Example 1:
# Input: sentence = "Hello, World! How are you?"
# Output: 'Hello World How are you'

# Example 2:
# Input: sentence = "Python 3.10: fast & clean."
# Output: 'Python 310 fast  clean'

import string

sentence = "Hello, World! How are you?"
clean = "".join(ch for ch in sentence if ch not in string.punctuation)
print(clean)

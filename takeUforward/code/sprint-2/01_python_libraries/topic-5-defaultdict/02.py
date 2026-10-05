# Group words by their first character using defaultdict(list).

# Example 1:
# Input: words = ["apple", "banana", "apricot", "cherry", "blueberry"]
# Output: {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

# Example 2:
# Input: words = ["dog", "cat", "deer"]
# Output: {'d': ['dog', 'deer'], 'c': ['cat']}

from collections import defaultdict

words = ["apple", "banana", "apricot", "cherry", "blueberry"]
grouped = defaultdict(list)
for w in words:
    grouped[w[0]].append(w)
print(dict(grouped))

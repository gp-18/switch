# Group words by a key after sorting them by that key.

# Example 1:
# Input: words = ["cat", "dog", "cow", "duck", "ant"]; sort and group by first letter
# Output: 'a': ['ant'], 'c': ['cat', 'cow'], 'd': ['dog', 'duck']

# Example 2:
# Input: words = ["pie", "apple", "fig"]; sort and group by length
# Output: 3: ['pie', 'fig'], 5: ['apple']

import itertools

words = ["cat", "dog", "cow", "duck", "ant"]
sorted_words = sorted(words, key=lambda w: w[0])
grouped = {k: list(g) for k, g in itertools.groupby(sorted_words, key=lambda w: w[0])}
print(grouped)

# Rewrite a normal dictionary grouping solution using defaultdict and compare the two implementations.

# Example 1:
# Input: pairs = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot')]
# Output: Grouping with defaultdict eliminates KeyError checks and boilerplate initialization

# Example 2:
# Input: pairs = [(1, 'one'), (1, 'uno'), (2, 'two')]
# Output: {1: ['one', 'uno'], 2: ['two']}

from collections import defaultdict

pairs = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot')]
grouped = defaultdict(list)
for category, item in pairs:
    grouped[category].append(item)
print(dict(grouped))

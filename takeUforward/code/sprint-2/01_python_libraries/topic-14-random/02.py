# Select a random element from a list.

# Example 1:
# Input: items = ['apple', 'banana', 'cherry']; random.choice(items)
# Output: One randomly selected element from items

# Example 2:
# Input: items = [10, 20, 30]
# Output: One randomly selected number from items

import random

items = ['apple', 'banana', 'cherry']
chosen = random.choice(items)
print(f"Random choice: {chosen}")

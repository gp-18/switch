# You need to find the top 5 most frequent numbers. Which library or combination of libraries would you consider?

# Example 1:
# Input: Requirement: Find top 5 frequent elements from list of numbers
# Output: collections.Counter with Counter.most_common(5) or heapq

# Example 2:
# Input: nums = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4]
# Output: Counter(nums).most_common(2) -> [(4, 4), (2, 3)]

from collections import Counter

# Answer: collections.Counter using Counter.most_common(k)
nums = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4]
top_2 = Counter(nums).most_common(2)
print(f"Top frequent: {top_2}")

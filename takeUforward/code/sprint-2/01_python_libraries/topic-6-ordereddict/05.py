# Explain why a normal modern Python dictionary and OrderedDict are not identical in terms of available ordering operations.

# Example 1:
# Input: Comparing dict and OrderedDict
# Output: OrderedDict has move_to_end(), popitem(last=False), and order-sensitive equality checking

# Example 2:
# Input: OrderedDict([('a', 1), ('b', 2)]) == OrderedDict([('b', 2), ('a', 1)])
# Output: False (order matters for OrderedDict equality)


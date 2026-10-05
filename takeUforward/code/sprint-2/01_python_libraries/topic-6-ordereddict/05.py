# Explain why a normal modern Python dictionary and OrderedDict are not identical in terms of available ordering operations.

# Example 1:
# Input: Comparing dict and OrderedDict
# Output: OrderedDict has move_to_end(), popitem(last=False), and order-sensitive equality checking

# Example 2:
# Input: OrderedDict([('a', 1), ('b', 2)]) == OrderedDict([('b', 2), ('a', 1)])
# Output: False (order matters for OrderedDict equality)

from collections import OrderedDict

od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
print(f"OrderedDict equality respecting order: {od1 == od2}")
print("OrderedDict supports move_to_end() and popitem(last=False) in O(1).")

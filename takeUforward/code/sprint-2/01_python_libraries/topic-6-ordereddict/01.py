# Create an OrderedDict and move one key to the end.

# Example 1:
# Input: od = OrderedDict([('a', 1), ('b', 2), ('c', 3)]); od.move_to_end('a')
# Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Example 2:
# Input: od = OrderedDict([('x', 10), ('y', 20)]); od.move_to_end('x')
# Output: OrderedDict([('y', 20), ('x', 10)])

from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od.move_to_end('a')
print(od)

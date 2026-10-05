# Access named-tuple fields using both field names and indexes.

# Example 1:
# Input: Item = namedtuple('Item', ['name', 'price']); it = Item('Book', 500)
# Output: it.name == it[0] == 'Book', it.price == it[1] == 500

# Example 2:
# Input: Pair = namedtuple('Pair', ['first', 'second']); p = Pair(1, 2)
# Output: p.first == p[0] == 1

from collections import namedtuple

Item = namedtuple('Item', ['name', 'price'])
it = Item('Book', 500)
print(f"By name: {it.name}, {it.price}")
print(f"By index: {it[0]}, {it[1]}")

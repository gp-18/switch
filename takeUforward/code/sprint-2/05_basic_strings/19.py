# Isomorphic Strings
# Two strings `s` and `t` are isomorphic if characters in `s` can be replaced to get `t`, preserving character order and maintaining a one-to-one character mapping.
#
# Example 1:
# Input: s = 'egg', t = 'add'
# Output: True  # 'e' -> 'a', 'g' -> 'd'
#
# Example 2:
# Input: s = 'foo', t = 'bar'
# Output: False  # 'o' cannot map to both 'a' and 'r'
#
# Example 3 (Edge Case - Two Characters Mapping to Same Character):
# Input: s = 'badc', t = 'baba'
# Output: False  # 'd' and 'b' cannot both map to 'b'

# Isomorphic Strings
# Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`, preserving order and ensuring a one-to-one mapping with no two characters mapping to the same character.
#
# Example 1:
# Input: s = 'egg', t = 'add'
# Output: True  # 'e' -> 'a', 'g' -> 'd'
#
# Example 2:
# Input: s = 'foo', t = 'bar'
# Output: False  # 'o' cannot map to both 'a' and 'r'
#
# Example 3 (Edge Case - Two Characters Mapping to Same Target):
# Input: s = 'badc', t = 'baba'
# Output: False  # 'd' and 'b' cannot both map to 'b'

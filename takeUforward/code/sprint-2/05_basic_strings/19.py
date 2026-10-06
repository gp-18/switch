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

s = input("Enter the first string : ")
t = input("Enter the second string : ")

print(f"Your strings are : '{s}' and '{t}' and now doing the operations on it.")

if len(s) != len(t):
    print("False")
else:
    map_s_to_t = {}
    map_t_to_s = {}
    is_isomorphic = True

    for char_s, char_t in zip(s, t):
        if char_s in map_s_to_t and map_s_to_t[char_s] != char_t:
            is_isomorphic = False
            break
        if char_t in map_t_to_s and map_t_to_s[char_t] != char_s:
            is_isomorphic = False
            break
        map_s_to_t[char_s] = char_t
        map_t_to_s[char_t] = char_s

    print(is_isomorphic)


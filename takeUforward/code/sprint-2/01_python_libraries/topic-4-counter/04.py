# Check whether two strings are anagrams using frequency counts.

# Example 1:
# Input: s1 = "listen", s2 = "silent"
# Output: True

# Example 2:
# Input: s1 = "hello", s2 = "world"
# Output: False

from collections import Counter

s1 = "listen"
s2 = "silent"
is_anagram = Counter(s1) == Counter(s2)
print(is_anagram)

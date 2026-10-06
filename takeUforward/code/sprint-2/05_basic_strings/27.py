# Find the Index of the First Occurrence in a String
# Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.
#
# Example 1:
# Input: haystack = 'sadbutsad', needle = 'sad'
# Output: 0
#
# Example 2:
# Input: haystack = 'leetcode', needle = 'leeto'
# Output: -1
#
# Example 3 (Edge Case - Needle at the End):
# Input: haystack = 'abcde', needle = 'cde'
# Output: 2

haystack = input("Enter the haystack string : ")
needle = input("Enter the needle string : ")

print(f"Haystack : '{haystack}', Needle : '{needle}' and now doing the operations on it.")

index = haystack.find(needle)
print(index)


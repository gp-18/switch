# Count Frequency of Characters in a String
# Given a string `s`, count and return the frequency of each character using character hashing or a hash map.
#
# Example 1:
# Input: s = 'banana'
# Output: {'b': 1, 'a': 3, 'n': 2}
#
# Example 2:
# Input: s = 'apple'
# Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}
#
# Example 3 (Edge Case - String with Spaces and Punctuation):
# Input: s = 'a b a!'
# Output: {'a': 2, ' ': 2, 'b': 1, '!': 1}

s = input("Enter the string : ")

print(f"Your string is : {s} and now doing the operations on it.")

freq = {}
for char in s : 
    freq[char] = freq.get(char, 0) + 1 

print(f"Your frequency map has become : {freq}")
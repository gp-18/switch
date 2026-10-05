# First Non-Repeating Character in a String
# Given a string `s`, find and return the first non-repeating character (or its index). If all characters repeat, return -1.
#
# Example 1:
# Input: s = 'leetcode'
# Output: 'l'  # Index 0 ('l' appears only once)
#
# Example 2:
# Input: s = 'loveleetcode'
# Output: 'v'  # Index 2 ('v' is the first unique character)
#
# Example 3 (Edge Case - All Characters Repeat):
# Input: s = 'aabb'
# Output: -1  # No unique character

s = input("Enter the string : ")

print(f"Your string is : {s} and now doing the operations on it.")

freq = {}

for char in s : 
    freq[char] = freq.get(char, 0) + 1 


for char in s : 
    if freq[char] == 1 : 
        print(char)
        break
else : 
    print("-1")
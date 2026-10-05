# Count Distinct Characters in a String
# Given a string `s`, count and return the number of distinct (unique) characters present in it.
#
# Example 1:
# Input: s = 'hello'
# Output: 4  # Distinct: 'h', 'e', 'l', 'o'
#
# Example 2:
# Input: s = 'aaaa'
# Output: 1  # Distinct: 'a'
#
# Example 3 (Edge Case - Mixed Case & Spaces):
# Input: s = 'aA 1'
# Output: 4  # 'a', 'A', ' ', '1' are all distinct

s = input("Enter the string : ")

print(f"Your string is : {s} and now doing the operations on it.")

freq = {}
for char in s : 
    freq[char] = freq.get(char, 0) + 1 

print(len(freq))
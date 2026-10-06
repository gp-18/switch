# Remove Vowels from a String
# Given a string `s`, remove all vowel characters ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') and return the remaining string.
#
# Example 1:
# Input: s = 'takeuforward'
# Output: 'tkfrwrd'
#
# Example 2:
# Input: s = 'hello'
# Output: 'hll'
#
# Example 3 (Edge Case - String of Only Vowels):
# Input: s = 'aeiouAEIOU'
# Output: ''

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")

vowels = "aeiouAEIOU"
result = ""

for char in s:
    if char not in vowels:
        result += char

print(f"String without vowels : {result}")


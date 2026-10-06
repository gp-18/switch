# Reverse Vowels of a String
# Given a string `s`, reverse only all the vowels in the string and return it. The vowels are 'a', 'e', 'i', 'o', and 'u' in both lower and upper cases.
#
# Example 1:
# Input: s = 'IceCreAm'
# Output: 'AceCreIm'
#
# Example 2:
# Input: s = 'leetcode'
# Output: 'leotcede'
#
# Example 3 (Edge Case - No Vowels in String):
# Input: s = 'xyz'
# Output: 'xyz'

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")

chars = list(s)
vowels = "aeiouAEIOU"
left = 0
right = len(chars) - 1

while left < right:
    while left < right and chars[left] not in vowels:
        left += 1
    while left < right and chars[right] not in vowels:
        right -= 1
    if left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

result = "".join(chars)
print(f"String after reversing vowels : {result}")


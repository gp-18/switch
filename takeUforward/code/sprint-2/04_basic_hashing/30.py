# Ransom Note
# Given two strings `ransomNote` and `magazine`, return True if `ransomNote` can be constructed using the letters from `magazine` (each letter in `magazine` can only be used once), otherwise False.
#
# Example 1:
# Input: ransomNote = 'a', magazine = 'b'
# Output: False
#
# Example 2:
# Input: ransomNote = 'aa', magazine = 'aab'
# Output: True
#
# Example 3 (Edge Case - Insufficient Frequency in Magazine):
# Input: ransomNote = 'aa', magazine = 'ab'
# Output: False  # 'magazine' has only one 'a'

ransomNote = input("Enter the ransom note string : ")
magazine = input("Enter the magazine string : ")

print(f"Your ransomNote is : '{ransomNote}' and magazine is : '{magazine}' and now doing the operations on it.")

freq = {}

for char in magazine:
    freq[char] = freq.get(char, 0) + 1

can_construct = True

for char in ransomNote:
    if char not in freq or freq[char] == 0:
        can_construct = False
        break

    freq[char] -= 1

print(can_construct)
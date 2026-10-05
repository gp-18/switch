# Check if Two Strings are Anagrams
# Given two strings `s` and `t`, return True if `t` is an anagram of `s` (contains the exact same characters with the same frequencies), and False otherwise.
#
# Example 1:
# Input: s = 'anagram', t = 'nagaram'
# Output: True
#
# Example 2:
# Input: s = 'rat', t = 'car'
# Output: False
#
# Example 3 (Edge Case - Different Lengths / Case Sensitive):
# Input: s = 'a', t = 'ab'
# Output: False

s = input("Enter the first string : ")
t = input("Enter the second string : ")

print(f"Your strings are : '{s}' and '{t}' and now doing the operations on it.")

if len(s) != len(t):
    print("False")
else:
    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    is_anagram = False

    for char in t:
        if char in freq and freq[char] > 0:
            freq[char] -= 1
        else:
            break
    else:
        is_anagram = True

    print(is_anagram)
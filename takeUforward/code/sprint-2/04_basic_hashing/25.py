# Sort Characters by Frequency
# Given a string `s`, sort the characters in decreasing order based on the frequency of each character. Return the sorted string.
#
# Example 1:
# Input: s = 'tree'
# Output: 'eert'  # 'e' appears twice, 'r' and 't' appear once ('eetr' is also valid)
#
# Example 2:
# Input: s = 'cccaaa'
# Output: 'aaaccc'  # Both 'a' and 'c' appear 3 times
#
# Example 3 (Edge Case - Case Sensitivity):
# Input: s = 'Aabb'
# Output: 'bbAa'  # 'b': 2, 'A': 1, 'a': 1 ('A' and 'a' are distinct)

s = input("Enter the string : ")

print(f"Your string is : {s} and now doing the operations on it.")



freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

result = ""

while freq:
    highest_frequency = 0
    highest_character = ""

    for char in freq:
        if freq[char] > highest_frequency:
            highest_frequency = freq[char]
            highest_character = char

    result += highest_character * highest_frequency

    del freq[highest_character]

print(f"The string sorted by frequency is : {result}")
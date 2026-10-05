# Check if String Can be Rearranged to a Palindrome
# Given a string `s`, determine whether the characters can be rearranged to form a palindrome. Return True if possible, otherwise False.
#
# Example 1:
# Input: s = 'civic'
# Output: True  # Already a palindrome
#
# Example 2:
# Input: s = 'ivicc'
# Output: True  # Can be rearranged to 'civic'
#
# Example 3 (Edge Case - Multiple Characters with Odd Counts):
# Input: s = 'aabbcd'
# Output: False  # 'c' and 'd' have odd frequencies (2 odd counts > 1)


s = input("Enter the string : ")

print(f"Your string is : {s} and now doing the operations on it.")

freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

odd_count = 0

for char in freq:
    if freq[char] % 2 != 0:
        odd_count += 1

if odd_count <= 1:
    print("True")
else:
    print("False")
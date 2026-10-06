# First Unique Character in a String
# Given a string `s`, find the first non-repeating character and return its index. If it does not exist, return -1.
#
# Example 1:
# Input: s = 'leetcode'
# Output: 0  # 'l' is at index 0
#
# Example 2:
# Input: s = 'loveleetcode'
# Output: 2  # 'v' is at index 2
#
# Example 3 (Edge Case - All Characters Repeat):
# Input: s = 'aabb'
# Output: -1

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")

freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

for i in range(len(s)):
    if freq[s[i]] == 1:
        print(i)
        break
else:
    print(-1)


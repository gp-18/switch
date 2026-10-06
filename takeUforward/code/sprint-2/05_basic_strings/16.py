# Reverse a String II
# Given a string `s` and an integer `k`, reverse the first `k` characters for every `2k` characters counting from the start of the string.
#
# Example 1:
# Input: s = 'abcdefg', k = 2
# Output: 'bacdfeg'
#
# Example 2:
# Input: s = 'abcd', k = 2
# Output: 'bacd'
#
# Example 3 (Edge Case - Fewer than k Characters Left):
# Input: s = 'abcdef', k = 4
# Output: 'dcbaef'  # Reverse first 4, remaining 2 intact

s = input("Enter the string : ")
k = int(input("Enter the value of k : "))

print(f"Your string is : '{s}', k = {k} and now doing the operations on it.")

chars = list(s)

for i in range(0, len(chars), 2 * k):
    chars[i:i + k] = reversed(chars[i:i + k])

result = "".join(chars)
print(f"Resulting string : '{result}'")


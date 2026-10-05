# Longest Common Prefix
# Find the longest common prefix string amongst an array of strings `strs`. If there is no common prefix, return an empty string `""`.
#
# Example 1:
# Input: strs = ['flower', 'flow', 'flight']
# Output: 'fl'
#
# Example 2:
# Input: strs = ['dog', 'racecar', 'car']
# Output: ''
#
# Example 3 (Edge Case - Single String in List):
# Input: strs = ['apple']
# Output: 'apple'

length = int(input("Enter the number of strings : "))
strs = []

for i in range(length):
    value = input(f"Enter string at index {i} : ")
    strs.append(value)

print(f"Your array of strings is : {strs} and now doing the operations on it.")

# Frequency of a Digit
# Count how many times a particular digit d occurs in a number n.
#
# Example 1:
# Input: n = 122333, d = 3
# Output: 3
#
# Example 2:
# Input: n = 45678, d = 9
# Output: 0
#
# Example 3 (Edge Case - Negative Number with Target Digit):
# Input: n = -12234, d = 2
# Output: 2


number = input("Enter the number : ")

freq = {}

for i in number : 
    freq[i] = freq.get(i,0) + 1

digit = input("Enter the digit : ")

print(freq[digit])
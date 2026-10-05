# Sum of Numbers From 1 to N
# Calculate the sum of numbers from 1 to N (1 + 2 + 3 + ... + N).
#
# Example 1:
# Input: n = 5
# Output: 15
#
# Example 2:
# Input: n = 10
# Output: 55
#
# Example 3 (Edge Case - Smallest Value N = 1):
# Input: n = 1
# Output: 1

number = int(input("Enter the number : "))

if number > 1 : 
  ans = number * (number + 1 ) // 2 

print(ans)
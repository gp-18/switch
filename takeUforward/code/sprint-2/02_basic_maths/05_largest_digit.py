# Find Largest Digit
# Find the largest digit present in an integer n.
#
# Example 1:
# Input: n = 58321
# Output: 8
#
# Example 2:
# Input: n = 24680
# Output: 8
#
# Example 3 (Edge Case - Negative Number):
# Input: n = -945
# Output: 9

number = abs(int(input("Enter the number : ")))

largest = float("-inf")

while number > 0 : 
  last_digit = number % 10 
  
  if last_digit > largest : 
    largest = last_digit 

  number = number // 10 

print(largest)
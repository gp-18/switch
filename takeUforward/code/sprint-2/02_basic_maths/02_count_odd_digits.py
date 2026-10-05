# Count Odd Digits
# Given an integer n, count how many digits are odd.
#
# Example 1:
# Input: n = 123456
# Output: 3  # Digits: 1, 3, 5
#
# Example 2:
# Input: n = 2468
# Output: 0
#
# Example 3 (Edge Case - Negative Number):
# Input: n = -13579
# Output: 5  # Digits: 1, 3, 5, 7, 9

number = abs(int(input("Enter the number : "))) 

odd_count = 0 

while number > 0 : 
  last_digit = number % 10 
  
  if last_digit % 2 != 0 : 
      odd_count += 1 

  number = number // 10 
  
print(odd_count)
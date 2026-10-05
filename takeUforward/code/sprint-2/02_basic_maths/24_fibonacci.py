# Fibonacci Number
# Find the nth Fibonacci number (0, 1, 1, 2, 3, 5, 8, 13... where F(0) = 0, F(1) = 1).
#
# Example 1:
# Input: n = 6
# Output: 8
#
# Example 2:
# Input: n = 7
# Output: 13
#
# Example 3 (Edge Case - Base Case Zero):
# Input: n = 0
# Output: 0

0 , 1 , 2 , 3 , 5 , 8 
1 , 2 , 3 , 4 , 5 , 6 
number = int(input("Enter the number : "))

if number > 0 : 
  a = 0 
  b = 1 

  for i in range(number) :
      a , b = b , a + b 

  print(a)


# default = a = 0 , b = 1 
# 0 = a = 1 , b = 1 
# 1 = a = 1 , b = 2 
# 2 = a = 2 , b = 3 
# 3 = a = 3 , b = 5 
# 4 = a = 5 , b = 8 
# 5 = a = 8 , b = 13 
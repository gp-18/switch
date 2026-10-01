# Pattern 3: Right-Angled Triangle of Numbers
# Given an integer N, print a right-angled triangle with numbers from 1 to i in each row.

# Example 1:
# Input: N = 3
# Output:
# 1
# 12
# 123

# Example 2:
# Input: N = 4
# Output:
# 1
# 12
# 123
# 1234


number = int(input("Enter the number : "))

for i in range( 1 , number + 1 ) :
    for j in range( 1 , i + 1 ) :
        print( j , end = "" )
    print()
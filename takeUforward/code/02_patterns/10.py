# Pattern 10: Half Diamond Star Pattern
# Given an integer N, print a half diamond star pattern of (2N - 1) rows.

# Example 1:
# Input: N = 3
# Output:
# *
# **
# ***
# **
# *

# Example 2:
# Input: N = 4
# Output:
# *
# **
# ***
# ****
# ***
# **
# *


number = int(input("Enter the number :"))

for i in range(1 , number + 1 ) :
    for j in range( 1 , i+1 ) :
        print( "*" , end = "" ) 
    print()


for i in range(1 , number ) :
    for j in range ( 1 , number - i + 1 ) : 
        print("*", end = "")
    print()
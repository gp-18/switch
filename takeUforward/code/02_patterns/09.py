# Pattern 9: Diamond Star Pattern
# Given an integer N, print a diamond star pattern of 2N rows.

# Example 1:
# Input: N = 3
# Output:
#   *
#  ***
# *****
# *****
#  ***
#   *

# Example 2:
# Input: N = 4
# Output:
#    *
#   ***
#  *****
# *******
# *******
#  *****
#   ***
#    *


number = int(input("Enter the number : "))

for i in range( 1 , number + 1 ) :
    for j in range( number - i ) :
        print(" " , end="")
    for k in range( 2*i -1 ) :
        print("*" , end = "")
    for l in range( number - i ) :
        print( " " , end = "" )
    print()

for i in range(1, number + 1):

    for j in range(i - 1):
        print(" ", end="")

    for k in range(2 * (number - i) + 1):
        print("*", end="")

    for l in range(i - 1):
        print(" ", end="")

    print()
    
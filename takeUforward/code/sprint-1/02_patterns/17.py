# Pattern 17: Alpha-Hill Pattern
# Given an integer N, print a centered pyramid of letters where row i has leading spaces, letters ascending from 'A' up to the i-th letter, and then descending back to 'A'.

# Example 1:
# Input: N = 3
# Output:
#   A
#  ABA
# ABCBA

# Example 2:
# Input: N = 4
# Output:
#    A
#   ABA
#  ABCBA
# ABCDCBA


number = int(input("Enter the number : "))

for i in range(1 , number + 1 ) :
    for j in range( 1 , number - i + 1 ) :
        print(" " , end = "")
    for k in range( 1 , i + 1 ) :
        print(chr(ord("A") + k - 1 ), end = "")
    for l in range( 1 , i ) :
        print(chr(ord("A") + i - l - 1 ), end = "")
    print()

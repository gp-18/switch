# Pattern 1: Square of Stars
# Given an integer N, print an N x N square of stars.

# Example 1:
# Input: N = 3
# Output:
# ***
# ***
# ***

# Example 2:
# Input: N = 4
# Output:
# ****
# ****
# ****
# ****

number = int(input("Enter the number : "))


for i in range( 1, number +1 ) :
    for j in range( 1 , number + 1 ) :
        print( "*" , end= "")
    print()
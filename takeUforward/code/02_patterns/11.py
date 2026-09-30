# Pattern 11: Binary Number Triangle
# Given an integer N, print a right-angled triangle of alternating 1s and 0s.

# Example 1:
# Input: N = 3
# Output:
# 1
# 01
# 101

# Example 2:
# Input: N = 4
# Output:
# 1
# 01
# 101. 
# 0101


number = int(input("Enter the number : "))

for i in range( 1 , number + 1 ) :
    for j in range( i) :
        if ( i + j ) % 2 == 0 :
            print("1" , end = "" ) 
        else :
            print("0" , end = "" ) 
    print()

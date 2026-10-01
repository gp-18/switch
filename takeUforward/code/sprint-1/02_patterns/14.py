# Pattern 14: Increasing Letter Triangle
# Given an integer N, print a right-angled triangle of letters starting from 'A' up to the (i+1)-th letter on each row.

# Example 1:
# Input: N = 3
# Output:
# A
# AB
# ABC

# Example 2:
# Input: N = 4
# Output:
# A
# AB
# ABC
# ABCD

number = int(input("Enter the number : "))

for i in range(1 , number + 1 ) :
    for j in range( 1, i + 1 ) :
        print(chr(ord("A")+j-1), end = "")
    print()
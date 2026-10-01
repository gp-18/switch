# Pattern 15: Reverse Letter Triangle
# Given an integer N, print an inverted right-angled triangle of letters starting from 'A' to the (N - i)-th letter.

# Example 1:
# Input: N = 3
# Output:
# ABC
# AB
# A

# Example 2:
# Input: N = 4
# Output:
# ABCD
# ABC
# AB
# A


number = int(input("Enter the number : "))

for i in range ( 1 , number + 1 ) :
    for j in range( 1 , number - i + 2 ) :
        print(chr(ord("A")+j-1), end = "")
    print()

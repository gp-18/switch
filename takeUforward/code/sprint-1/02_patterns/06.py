# Pattern 6: Inverted Right-Angled Triangle of Numbers
# Given an integer N, print an inverted right-angled triangle with numbers from 1 to (N - i + 1).

# Example 1:
# Input: N = 3
# Output:
# 123
# 12
# 1

# Example 2:
# Input: N = 4
# Output:
# 1234
# 123
# 12
# 1


number = int(input("Enter the number : "))

for i in range( 1 , number + 1 ) :
    for j in range( 1 , number - i + 2 ) : 
        print(j , end="")
    print()
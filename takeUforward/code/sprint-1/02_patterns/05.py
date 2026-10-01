# Pattern 5: Inverted Right-Angled Triangle of Stars
# Given an integer N, print an inverted right-angled triangle of stars of height N.

# Example 1:
# Input: N = 3
# Output:
# ***
# **
# *

# Example 2:
# Input: N = 4
# Output:
# ****
# ***
# **
# *

number = int(input("Enter the number : ")) 

for i in range(0, number + 1 ) :
    for j in range ( 0, number - i + 1 ) :
        print("*" , end ="")
    print()


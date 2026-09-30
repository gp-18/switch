# Pattern 12: Number Crown
# Given an integer N, print a number crown pattern of height N with numbers increasing, spaces in between, and numbers decreasing.

# Example 1:
# Input: N = 3
# Output:
# 1    1
# 12  21
# 123321

# Example 2:
# Input: N = 4
# Output:
# 1      1
# 12    21
# 123  321
# 12344321


number = int(input("Enter the number : "))

for i in range ( 1 , number + 1 ) :
    for j in range ( 1 , i + 1 ) :
        print(j , end = "")
    for k in range ( 2 * ( number - i ) ) :
        print(" " , end = "")
    for l in range ( 1 , i + 1 ) :
        print( i - l + 1 , end = "" ) 
    print()


# Pattern 16: Alpha-Ramp Pattern
# Given an integer N, print a right-angled triangle where the i-th row contains the i-th uppercase letter repeated i times.

# Example 1:
# Input: N = 3
# Output:
# A
# BB
# CCC

# Example 2:
# Input: N = 4
# Output:
# A
# BB
# CCC
# DDDD



number = int(input("Enter the number : "))

for i in range(1 , number + 1 ) :
    for j in range(1 , i + 1 ) :
        print(chr(ord("A") + i - 1 ), end = "")
    print()
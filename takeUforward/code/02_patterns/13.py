# Pattern 13: Increasing Number Triangle
# Given an integer N, print a right-angled triangle with continuous increasing numbers starting from 1 with spaces between numbers.

# Example 1:
# Input: N = 3
# Output:
# 1
# 2 3
# 4 5 6

# Example 2:
# Input: N = 4
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

number = int(input("Enter the number : "))

count = 1
for i in range(1 , number + 1 ) :
    for j in range(1 , i + 1 ) :
        print(count , end = " ")
        count += 1 
    print()
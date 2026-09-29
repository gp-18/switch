# Pattern 4: Row Number Repeated
# Given an integer N, print a right-angled triangle where the i-th row contains the number i repeated i times.

# Example 1:
# Input: N = 3
# Output:
# 1
# 22
# 333

# Example 2:
# Input: N = 4
# Output:
# 1
# 22
# 333
# 4444

number = int(input("Enter the number : ")) 

for i in range(1 , number + 1 ) :
    for j in range(1 , i+1 ) :
        print(i , end="")
    print()
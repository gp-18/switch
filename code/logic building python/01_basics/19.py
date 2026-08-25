# Print all odd numbers between 1 and 100.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

for i in range(1 , 101):
    if i & 1 !=0 : 
        print(i)

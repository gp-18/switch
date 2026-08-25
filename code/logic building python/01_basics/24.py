# Print the sum of all odd numbers up to n.
# Example 1: Input: 5 -> Output: 15
# Example 2: Input: 10 -> Output: 55

number = int(input("Enter the number : "))
answer = 0 

for i in range(1 , number+1) :
    if i % 2 !=0 : 
        answer = answer + i 

print(answer)

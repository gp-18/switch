# Print the sum of all even numbers up to n.

number = int(input("Enter the number : "))
answer = 0

for i in range(1 , number+1) :
    if i & 1 == 0 : 
        answer = answer + i 

print(answer)
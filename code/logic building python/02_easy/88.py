# Print the sum of first n terms of Fibonacci series.
# Example 1: Input: 5 -> Output: 0 1 1 2 3
# Example 2: Input: 3 -> Output: 0 1 1

if (number := int(input("Enter the number : "))) > 1 : 
    a = 0 
    b = 1
    total = 0  

    for i in range(number) :
        total = total + a 
        a , b = b , a + b

    print(total)

     
else : 
    print("enter the correct number")

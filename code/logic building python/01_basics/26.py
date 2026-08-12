# Print the squares of numbers from 1 to n.

if (number := int(input("Enter the number : "))) >= 0 :
    for i in range(1 , number+1) :
        print(f"The square of {i} is : {i*i}")
# Print the factorial of a given number using a loop.

if (number := int(input("Enter the number: "))) > 0:
    answer = 1 

    for i in range(1 , number+1) :
        answer = answer * i 

    print(answer) 

else:
    print("Number must be greater than or equal to 0.")


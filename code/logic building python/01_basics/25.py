# Print the factorial of a given number using a loop.
# Example 1: Input: 5 -> Output: 120
# Example 2: Input: 3 -> Output: 6

if (number := int(input("Enter the number: "))) > 0:
    answer = 1 

    for i in range(1 , number+1) :
        answer = answer * i 

    print(answer) 

else:
    print("Number must be greater than or equal to 0.")

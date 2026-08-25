# Print the cubes of numbers from 1 to n.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (number := int(input("Enter the number : "))) >= 0 :
    for i in range(1 , number+1) :
        print(f"The cube of {i} is : {i*i*i}")

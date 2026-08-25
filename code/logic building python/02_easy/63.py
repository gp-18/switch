# Take a 4-digit number and check if the first and last digits are equal.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

number = list(map(int, input("Enter the 4 digit number :")))

if len(number) != 4 : 
    print("Enter the correct length")

if number[0] == number[len(number) -1 ] :
    print("yes first and last digit is equal")
else : 
    print("no it's not equal")

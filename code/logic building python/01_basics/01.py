# Take a number and print whether it's positive, negative, or zero.
# Example 1: Input: 5 -> Output: the number is positive
# Example 2: Input: -5 -> Output: the number is negative

number = int(input("Enter the number : "))


if number < 0 :
    print("the number is negative")
elif number == 0 : 
    print("the number is 0")
else : 
    print("the number is positive")

# Check if a number is even or odd.
# Example 1: Input: 4 -> Output: the number is even
# Example 2: Input: 7 -> Output: the number is odd

number = int(input("Enter the number : "))


if number & 1 :
    print("The number is odd")
else : 
    print("The number is even")

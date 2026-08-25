# Check if a number is divisible by both 3 and 5.
# Example 1: Input: 15 -> Output: divisible by both 3 and 5
# Example 2: Input: 10 -> Output: not divisible by both 3 and 5

number = int(input("Enter the number : "))


if number % 3 == 0 and number % 5 == 0 : 
    print("yes divisible by both 3 and 5")
else : 
    print("no not divisible by 3 and 5")

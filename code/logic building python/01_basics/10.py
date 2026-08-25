# Take a character and check whether it's uppercase, lowercase, a digit, or a special character.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

character = input("Enter the character : ")

if character.isupper() :
    print("uppercase")
elif character.islower() :
    print("lowercase")
elif character.isdigit() :
    print("digit")
else : 
    print("special case")

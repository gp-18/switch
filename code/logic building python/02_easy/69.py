# Take a character and check if it is a letter, a digit, or neither.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

character = input("Enter the character: ")

if len(character) != 1:
    print("Only one character is allowed")
elif character.isdigit():
    print("Yes, it's a digit")
elif character.isalpha():
    print("Yes, it's a letter")
else:
    print("Neither")

# Take a password string and check basic rules (length >= 8 and contains at least one digit).
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

password = input("Enter the string: ")

if len(password) >= 8 and any(character.isdigit() for character in password):
    print("Yes")
else:
    print("No")

# Count how many uppercase and lowercase letters a string has.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (string := input("Enter the string: ")):
    uppercase = 0
    lowercase = 0

    for char in string:
        if 'A' <= char <= 'Z':
            uppercase += 1

        elif 'a' <= char <= 'z':
            lowercase += 1

    print("Uppercase letters:", uppercase)
    print("Lowercase letters:", lowercase)

else:
    print("Enter a valid string")

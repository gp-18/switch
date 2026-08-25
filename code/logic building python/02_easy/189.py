# Check if a given string is a binary string.
# Example 1: Input: '10101001' -> Output: Yes, it is a binary string
# Example 2: Input: '10102001' -> Output: No, it is not a binary string

text = input("Enter a string: ")

if len(text) > 0 and all(char in "01" for char in text):
    print("Yes, it is a binary string")
else:
    print("No, it is not a binary string")

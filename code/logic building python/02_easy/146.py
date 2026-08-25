# Reverse a string without using built-in reverse.
# Example 1: Input: 'hello' -> Output: olleh
# Example 2: Input: 1234 -> Output: 4321

if (string := input("Enter the string: ")) and len(string) >= 1:

    reverse = ""
    for char in string : 
        reverse = char + reverse

    print(reverse)

else:
    print("Enter a valid string")

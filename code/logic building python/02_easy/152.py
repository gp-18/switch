# Remove all spaces from a string.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (string := input("Enter the string: ")):

    new_string = ""

    for char in string:
        if char != " ":
            new_string += char

    print(new_string)

else:
    print("Enter a valid string")

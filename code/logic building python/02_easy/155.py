# Print the string after removing all digit characters.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (string := input("Enter the string: ")) and len(string) >= 1:

    new_string = ""

    for char in string:
        if not char.isdigit():
            new_string += char

    print(new_string)

else:
    print("Give correct string")

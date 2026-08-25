# Swap case: convert uppercase to lowercase and lowercase to uppercase.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (string := input("Enter the string: ")):

    new_string = ""

    for char in string:
        if char.islower():
            new_string += char.upper()

        elif char.isupper():
            new_string += char.lower()

        else:
            new_string += char

    print(new_string)

else:
    print("Enter a valid string")

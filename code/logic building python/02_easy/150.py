# Remove the first and last character of a string and print the remaining.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (string := input("Enter the string: ")) and len(string) >= 2:

    new_string = ""

    for i in range(1, len(string) - 1):
        new_string += string[i]

    print(new_string)

else:
    print("Enter a valid string with at least 2 characters")

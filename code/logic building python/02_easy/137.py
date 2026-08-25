# Count how many characters (excluding spaces) are in a string.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (string := input("Enter the string: ")) and len(string) >= 1:
    count = 0

    for char in string:
        if char != " ":
            count += 1

    print(count)

else:
    print("Enter a valid string")

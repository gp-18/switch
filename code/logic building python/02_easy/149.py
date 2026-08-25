# Print the middle character(s) of a string.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (string1 := input("Enter the string: ")) and len(string1) >= 1:

    mid = len(string1) // 2

    if len(string1) % 2 != 0:
        print(string1[mid])

    else:
        print(string1[mid - 1], string1[mid])

else:
    print("Enter the correct string1")

# Count how many words are in a sentence.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (string := input("Enter the string: ")) and len(string) >= 1:

    count = 0
    in_word = False

    for char in string:
        if char != " " and not in_word:
            count += 1
            in_word = True

        elif char == " ":
            in_word = False

    print(count)

else:
    print("Enter a valid string")

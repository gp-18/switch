# Print each word of a sentence on a new line.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (string := input("Enter the sentence: ")):

    word = ""

    for char in string:

        if char != " ":
            word += char

        else:
            if word != "":
                print(word)
                word = ""

    if word != "":
        print(word)

else:
    print("Enter a valid sentence")

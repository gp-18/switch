# Capitalize the first letter of each word in a sentence.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (string := input("Enter the sentence: ")):

    new_string = ""
    new_word = True

    for char in string:

        if char == " ":
            new_string += char
            new_word = True

        elif new_word:
            new_string += char.upper()
            new_word = False

        else:
            new_string += char

    print(new_string)

else:
    print("Enter a valid sentence")

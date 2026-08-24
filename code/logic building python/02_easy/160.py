# Print the sentence in title case
# (first letter of each word capital, remaining letters lowercase).

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
            new_string += char.lower()

    print(new_string)

else:
    print("Enter a valid sentence")
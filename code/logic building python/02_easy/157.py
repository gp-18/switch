# Print each word of a sentence on a new line.

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
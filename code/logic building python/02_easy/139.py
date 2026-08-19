# Compare two strings lexicographically (dictionary order).

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) >= 1 and len(string2) >= 1:

    result = 0
    minimum = min(len(string1), len(string2))

    for i in range(minimum):

        if string1[i] < string2[i]:
            result = -1
            break

        elif string1[i] > string2[i]:
            result = 1
            break

    if result == 0:

        if len(string1) < len(string2):
            result = -1

        elif len(string1) > len(string2):
            result = 1

    if result == -1:
        print("First string comes before second string")

    elif result == 1:
        print("First string comes after second string")

    else:
        print("Both strings are equal")

else:
    print("Enter valid strings")
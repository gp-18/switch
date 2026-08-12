# Convert all characters of a string to lowercase.

string = input("Enter the string: ")
print(string.lower())
new_string = ""

for value in string:
    if 65 <= ord(value) <= 90:
        cal = chr(ord(value) + 32)
        new_string = new_string + cal
    else:
        new_string = new_string + value

print(new_string)
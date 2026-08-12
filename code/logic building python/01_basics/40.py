# Convert all characters of a string to uppercase.

string = str(input("Enter the string : "))

string_upper = string.upper()

print(string_upper)
new_string = ""

for value in string : 
    if 97 <= ord(value) <= 122 :
        cal = chr(ord(value)-32)
        new_string = new_string + cal
# Convert all characters of a string to uppercase.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

string = str(input("Enter the string : "))

string_upper = string.upper()

print(string_upper)
new_string = ""

for value in string : 
    if 97 <= ord(value) <= 122 :
        cal = chr(ord(value)-32)
        new_string = new_string + cal

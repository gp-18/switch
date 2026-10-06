# Toggle Case of Each Character
# Given a string `s`, convert all lowercase letters to uppercase and all uppercase letters to lowercase. Non-alphabetic characters should remain unchanged.
#
# Example 1:
# Input: s = 'Hello World'
# Output: 'hELLO wORLD'
#
# Example 2:
# Input: s = 'PyThOn'
# Output: 'pYtHoN'
#
# Example 3 (Edge Case - No Alphabetic Characters):
# Input: s = '123 #$%'
# Output: '123 #$%'

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")

toggled_string = ""
for char in s : 
    if char.isupper() : 
        toggled_string += char.lower()
    elif char.islower() : 
        toggled_string += char.upper()
    else : 
        toggled_string += char

print(f"Toggled string : {toggled_string}")
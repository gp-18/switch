# Count Digits in a String
# Given a string `s`, count how many characters are numeric digits ('0'-'9').
#
# Example 1:
# Input: s = 'user123abc45'
# Output: 5  # Digits: 1, 2, 3, 4, 5
#
# Example 2:
# Input: s = 'Hello World'
# Output: 0
#
# Example 3 (Edge Case - String of Only Digits):
# Input: s = '9876543210'
# Output: 10

s = input("Enter the string : ")

print(f"Your string is : '{s}' and now doing the operations on it.")


digit = 0 

for char in s : 
    if char.isdigit() :
        digit += 1 

print(f"Number of digits : {digit}")
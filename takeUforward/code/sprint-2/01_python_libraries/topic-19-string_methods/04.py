# Reverse a string and check whether it is a palindrome.

# Example 1:
# Input: s = "radar"
# Output: reversed: "radar", is_palindrome: True

# Example 2:
# Input: s = "python"
# Output: reversed: "nohtyp", is_palindrome: False

s = "radar"
rev = s[::-1]
is_palindrome = s == rev
print(f'reversed: "{rev}", is_palindrome: {is_palindrome}')

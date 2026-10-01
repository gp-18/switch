# Check whether a string is a palindrome after converting it to lowercase (first ignore spaces, then try ignoring spaces and punctuation).

# Example 1:
# Input: "Race car"
# Output: True (cleaned: "racecar")

# Example 2:
# Input: "hello"
# Output: False


import string

input_string = input("Enter a string: ")

# Part 1: Ignoring spaces only
cleaned_no_spaces = input_string.replace(" ", "").lower()
is_pal_spaces = cleaned_no_spaces == cleaned_no_spaces[::-1]
print(f'Ignoring spaces: "{cleaned_no_spaces}" -> Palindrome: {is_pal_spaces}')

# Part 2: Ignoring spaces and punctuation
cleaned_alphanumeric = "".join(ch for ch in input_string.lower() if ch.isalnum())
is_pal_all = cleaned_alphanumeric == cleaned_alphanumeric[::-1]
print(f'Ignoring spaces & punctuation: "{cleaned_alphanumeric}" -> Palindrome: {is_pal_all}')
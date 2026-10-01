# Check whether a string is empty.

# Example 1:
# Input: ""
# Output: The string is empty

# Example 2:
# Input: "Hello"
# Output: The string is not empty

text = input("Enter a string: ")

if len(text) == 0:
    print("The string is empty")
else:
    print("The string is not empty")

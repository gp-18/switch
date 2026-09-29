# Count how many times a chosen character appears in a string.

# Example 1:
# Input: string = "banana", char = "a"
# Output: 3

# Example 2:
# Input: string = "Mississippi", char = "s"
# Output: 4


string = input("Enter a string: ")
char = input("Enter a character to count: ")
count = string.count(char)
print(f'The character "{char}" appears {count} times in the string "{string}".')
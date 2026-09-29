# Replace every space in a sentence with a hyphen.

# Example 1:
# Input: "python is fun"
# Output: "python-is-fun"

# Example 2:
# Input: "data structures and algorithms"
# Output: "data-structures-and-algorithms"

text = input("Enter a sentence: ")
new_text = text.replace(" ", "-")
print(f'The modified sentence is: "{new_text}".')
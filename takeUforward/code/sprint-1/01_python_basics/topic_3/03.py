# Print the first three characters and the last three characters of a string.

# Example 1:
# Input: text = "programming"
# Output: First three: pro, Last three: ing

# Example 2:
# Input: text = "Python"
# Output: First three: Pyt, Last three: hon


text = input("Enter a string: ")
first_three = text[:3]
last_three = text[-3:]
print(f"First three: {first_three}, Last three: {last_three}")
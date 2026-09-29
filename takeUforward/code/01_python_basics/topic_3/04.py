# Reverse a string using slicing.

# Example 1:
# Input: text = "hello"
# Output: "olleh"

# Example 2:
# Input: text = "Python"
# Output: "nohtyP"



text = str(input("Enter a string: "))
normal_text = text[::1]
print(f"Normal string: {normal_text}")
reversed_text = text[::-1]
print(f"Reversed string: {reversed_text}")
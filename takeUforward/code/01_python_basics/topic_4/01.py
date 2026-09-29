# Take a user-entered name with extra spaces and inconsistent case; clean it and display it in title case.

# Example 1:
# Input: "   jOhN  dOE   "
# Output: "John Doe"

# Example 2:
# Input: "  aLiCe sMiTh "
# Output: "Alice Smith"


text = input("Enter your name: ") 
cleaned_text = text.strip().title()
print(cleaned_text)
# Ask for a birth year and calculate an approximate age using the current year supplied as another input.

# Example 1:
# Input: Enter your birth year: 2000, Enter the current year: 2026
# Output: You are approximately 26 years old.

# Example 2:
# Input: Enter your birth year: 1995, Enter the current year: 2024
# Output: You are approximately 29 years old.

birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))
age = current_year - birth_year
print(f"You are approximately {age} years old.")

# Check whether an email-like string ends with ".com" and whether a supplied code contains only letters and digits. State the limitations of these checks.

# Example 1:
# Input: email = "user@example.com", code = "PASS123"
# Output: Ends with .com: True, Code is alphanumeric: True

# Example 2:
# Input: email = "user@domain.org", code = "CODE-456"
# Output: Ends with .com: False, Code is alphanumeric: False (contains '-')

email = input("Enter an email-like string: ")
code = input("Enter a code: ")
ends_with_com = email.endswith(".com")
is_alphanumeric = code.isalnum()
print(f'Ends with .com: {ends_with_com}, Code is alphanumeric: {is_alphanumeric}.')

# Limitations of these checks:
print("\nLimitations of these checks:")
print("1. endswith('.com') only checks the suffix. It does not validate '@', domain name, or valid email structure.")
print("2. isalnum() only verifies that all characters are letters or digits. It does not enforce format, length, or permitted symbols.")
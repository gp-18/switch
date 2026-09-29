# Keep asking for a password until the correct password is entered (use a practice-only password, not a real one).

# Example 1:
# Input: "wrong1", "secret123" (correct)
# Output: "Incorrect password. Try again." -> "Access granted!"

# Example 2:
# Input: "secret123" (correct on first try)
# Output: "Access granted!"

correct_password = "secret123"

while True:
    entered_password = input("Enter password: ")
    if entered_password == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")

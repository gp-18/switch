# Extract the username from an email address.
# Example 1: Input: 'john.doe@example.com' -> Output: john.doe
# Example 2: Input: 'user123@gmail.com' -> Output: user123

email = input("Enter email address: ")

if "@" in email:
    username = email.split("@")[0]
    print("Username:", username)
else:
    print("Invalid email address")

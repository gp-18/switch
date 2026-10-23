# Q6. Secure User Account & Password Lock (Practice - Encapsulation)
#
# Task:
# Design a `UserAccount` class that encapsulates user authentication credentials,
# enforces minimum password standards, and automatically locks accounts after repeated failed logins.
#
# Attributes:
# - username (str) : Public username (public).
# - email (str) : Public email address (public).
# - __password (str) : Secret password string (private).
# - __failed_attempts (int) : Count of consecutive failed logins (private).
# - __is_locked (bool) : Flag indicating if the account is locked (private).
#
# Methods:
# - __init__(self, username: str, email: str, password: str):
#     Initializes account. Password must be at least 8 characters long.
# - login(self, attempted_password: str) -> bool:
#     If __is_locked is True, prints "Account is locked. Contact administrator." and returns False.
#     If attempted_password == self.__password, resets __failed_attempts = 0 and returns True.
#     Otherwise, increments __failed_attempts += 1. If __failed_attempts >= 3, sets __is_locked = True
#     and prints "Account locked due to 3 failed attempts.". Returns False.
# - change_password(self, old_pwd: str, new_pwd: str) -> bool:
#     Requires old_pwd == self.__password.
#     Requires len(new_pwd) >= 8 and new_pwd != old_pwd.
#     If valid, updates __password and returns True. Otherwise prints "Password change failed." and returns False.
# - unlock_account(self, admin_key: str) -> bool:
#     If admin_key == "ADMIN_KEY_999", unlocks account and resets failed attempts.
#
# Example 1:
# Input:
# user = UserAccount("john_doe", "john@example.com", "Secret@123")
# print("Login 1:", user.login("Wrong1"))
# print("Login 2:", user.login("Wrong2"))
# print("Login 3:", user.login("Wrong3"))  # Triggers lock
# print("Login 4:", user.login("Secret@123"))  # Fails because locked
# user.unlock_account("ADMIN_KEY_999")
# print("Login after unlock:", user.login("Secret@123"))
# Output:
# Login 1: False
# Login 2: False
# Account locked due to 3 failed attempts.
# Login 3: False
# Account is locked. Contact administrator.
# Login 4: False
# Login after unlock: True
#
# Example 2:
# Input:
# user = UserAccount("alice_w", "alice@example.com", "MyPass1234")
# print("Change Pwd:", user.change_password("MyPass1234", "NewPass5678"))
# print("Login with new:", user.login("NewPass5678"))
# Output:
# Change Pwd: True
# Login with new: True
#
# Example 3 (Edge Case):
# Input:
# user = UserAccount("bob_m", "bob@example.com", "OldPassword")
# # Attempt to change to short password (< 8 chars) or duplicate
# print("Change short:", user.change_password("OldPassword", "short"))
# print("Change same:", user.change_password("OldPassword", "OldPassword"))
# Output:
# Password change failed.
# Change short: False
# Password change failed.
# Change same: False
#
# Think About:
# - Security policies like lockout counters and password validation are strictly internal invariants.
# - Time Complexity: O(1) for login and password verification.
# - Space Complexity: O(1) auxiliary space.

# Write your UserAccount class below:

class UserAccount:
    def __init__(self, username: str, email: str, password: str):
        # Write your code here
        pass

    def login(self, attempted_password: str) -> bool:
        # Write your code here
        pass

    def change_password(self, old_pwd: str, new_pwd: str) -> bool:
        # Write your code here
        pass

    def unlock_account(self, admin_key: str) -> bool:
        # Write your code here
        pass

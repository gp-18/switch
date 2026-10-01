# ============================================================
# Problem: Notification System
# Difficulty: Hard
# ============================================================
#
# PROBLEM STATEMENT:
# Design a notification system with a common notification interface
# and separate EmailNotification, SMSNotification, and PushNotification
# implementations.
# Validate required data and provide send() returning status:
# - Email requires non-empty string with "@" and "."
# - SMS requires valid digits phone number (10 to 15 digits)
# - Push requires non-empty device token
# Process multiple notifications polymorphically.
#
# INPUT:
# - notifications_data: list of tuples (notification_type, recipient_data)
#
# OUTPUT:
# - List of status strings: "<type>: success" or "<type>: failure"
#
# EXAMPLE:
# Input:  [("email", "user@example.com"), ("sms", "9876543210"), ("push", "device123")]
# Output: ["email: success", "sms: success", "push: success"]
#
# CONSTRAINTS:
# - notification_type is in {"email", "sms", "push"}
# ============================================================

from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, recipient):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def send(self):
        pass


class EmailNotification(Notification):
    def validate(self):
        pass

    def send(self):
        pass


class SMSNotification(Notification):
    def validate(self):
        pass

    def send(self):
        pass


class PushNotification(Notification):
    def validate(self):
        pass

    def send(self):
        pass


def solution(notifications_data):
    # Process notifications polymorphically and return status list
    pass


# ---- TEST CASES ----
assert solution([
    ("email", "user@example.com"),
    ("sms", "9876543210"),
    ("push", "device123")
]) == [
    "email: success",
    "sms: success",
    "push: success"
], "Test 1 Failed"

assert solution([
    ("email", "invalidemail"),
    ("sms", "1234"),
    ("push", "")
]) == [
    "email: failure",
    "sms: failure",
    "push: failure"
], "Test 2 Failed"

print("All test cases passed!")

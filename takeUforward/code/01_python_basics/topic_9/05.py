# Demonstrate short-circuiting with and or or; explain why the second expression may not run.

# Example 1:
# Input: False and (10 / 0 == 0)
# Output: False (no ZeroDivisionError because False short-circuits 'and')

# Example 2:
# Input: True or (10 / 0 == 0)
# Output: True (no ZeroDivisionError because True short-circuits 'or')

# Short-circuiting explanation:
# 'and': Python stops evaluating as soon as an operand is False (since False and anything is False).
# 'or': Python stops evaluating as soon as an operand is True (since True or anything is True).

# Demonstration 1: 'and' short-circuiting
result_and = False and (10 / 0 == 0)
print(f"False and (10 / 0 == 0) -> {result_and}")
print("Explanation: The left operand is False, so Python skips the right operand (10 / 0 == 0), preventing a ZeroDivisionError.\n")

# Demonstration 2: 'or' short-circuiting
result_or = True or (10 / 0 == 0)
print(f"True or (10 / 0 == 0) -> {result_or}")
print("Explanation: The left operand is True, so Python skips the right operand (10 / 0 == 0), preventing a ZeroDivisionError.")

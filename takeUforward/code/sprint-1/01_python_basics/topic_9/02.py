# Check whether a person is eligible when both age and ID conditions must be met.

# Example 1:
# Input: age = 20, has_id = True (requires age >= 18 and has_id == True)
# Output: Eligible

# Example 2:
# Input: age = 16, has_id = True
# Output: Not eligible

age = int(input("Enter age: "))
has_id_input = input("Do you have a valid ID? (yes/no): ").strip().lower()
has_id = has_id_input in ("yes", "y", "true", "1")

if age >= 18 and has_id:
    print("Eligible")
else:
    print("Not eligible")

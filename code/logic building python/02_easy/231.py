# Check if a string's characters are in alphabetical order.
# Example 1: Input: 'abcde' -> Output: True
# Example 2: Input: 'edabit' -> Output: False

text = input("Enter a string: ")

is_sorted = list(text) == sorted(text)
if is_sorted:
    print("Characters are in alphabetical order")
else:
    print("Characters are not in alphabetical order")

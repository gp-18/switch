# Check if a string is an isogram (no repeating letters, case-insensitive).
# Example 1: Input: 'Algorism' -> Output: True
# Example 2: Input: 'PasSword' -> Output: False

text = input("Enter a string: ").lower()

is_isogram = len(text) == len(set(text))
if is_isogram:
    print("Yes, it is an isogram")
else:
    print("No, it is not an isogram")

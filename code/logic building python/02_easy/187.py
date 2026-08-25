# Remove the i-th character from a string.
# Example 1: Input: text='python', index=2 -> Output: pyhon
# Example 2: Input: text='hello', index=0 -> Output: ello

text = input("Enter a string: ")
index = int(input("Enter index to remove (0-indexed): "))

if 0 <= index < len(text):
    result = text[:index] + text[index + 1:]
    print("Resulting string:", result)
else:
    print("Invalid index")

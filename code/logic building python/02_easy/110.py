# Print all characters of a string one by one recursively.
# Example 1: Input: 'hello' -> Output: h e l l o
# Example 2: Input: 'py' -> Output: p y

def print_chars(s, index=0):
    if index >= len(s):
        return
    print(s[index], end=" ")
    print_chars(s, index + 1)

text = input("Enter a string: ")
print_chars(text)
print()

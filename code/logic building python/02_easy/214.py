# Double each character in a string.
# Example 1: Input: 'Hello' -> Output: HHeelllloo
# Example 2: Input: '123' -> Output: 112233

text = input("Enter a string: ")

doubled = "".join(c * 2 for c in text)
print("Doubled string:", doubled)

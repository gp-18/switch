# Sort a string's characters in alphabetical order.
# Example 1: Input: 'hello' -> Output: ehllo
# Example 2: Input: 'edabit' -> Output: abdeit

text = input("Enter a string: ")

sorted_chars = "".join(sorted(text))
print("Sorted string:", sorted_chars)

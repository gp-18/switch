# Replace all vowels in a string with a specified character.
# Example 1: Input: text='hello world', char='#' -> Output: h#ll# w#rld
# Example 2: Input: text='python', char='*' -> Output: pyth*n

text = input("Enter a string: ")
replacement = input("Enter replacement character: ")

vowels = "aeiouAEIOU"
result = "".join(replacement if char in vowels else char for char in text)
print("Resulting string:", result)

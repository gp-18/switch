# Replace all vowels in a string with a specified vowel.
# Example 1: Input: text='hello world', vowel='u' -> Output: hullu wurld
# Example 2: Input: text='python', vowel='o' -> Output: python

text = input("Enter a string: ")
target_vowel = input("Enter specified vowel: ")

vowels = "aeiouAEIOU"
result = "".join(target_vowel if char in vowels else char for char in text)
print("Resulting string:", result)

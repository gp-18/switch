# Count letters and digits in a sentence.
# Example 1: Input: 'hello world! 123' -> Output: LETTERS: 10, DIGITS: 3
# Example 2: Input: 'Python 3.10' -> Output: LETTERS: 6, DIGITS: 3

sentence = input("Enter a sentence: ")

letters = sum(c.isalpha() for c in sentence)
digits = sum(c.isdigit() for c in sentence)

print("LETTERS:", letters)
print("DIGITS:", digits)

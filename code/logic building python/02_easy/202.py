# Write a stutter function that repeats the first two letters of a word.
# Example 1: Input: 'incredible' -> Output: in... in... incredible?
# Example 2: Input: 'enthusiastic' -> Output: en... en... enthusiastic?

def stutter(word):
    if len(word) >= 2:
        first_two = word[:2]
        return f"{first_two}... {first_two}... {word}?"
    return word

text = input("Enter a word: ")
print(stutter(text))

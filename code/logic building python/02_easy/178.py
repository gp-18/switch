# Sort words in alphabetical order.
# Example 1: Input: 'python logic easy' -> Output: easy logic python
# Example 2: Input: 'banana apple' -> Output: apple banana

sentence = input("Enter a sentence: ")

words = sentence.split()
words.sort(key=str.lower)

print("Words in alphabetical order:")
for word in words:
    print(word)

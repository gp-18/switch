# Sort a comma-separated sequence of words alphabetically.
# Example 1: Input: 'without,hello,bag,world' -> Output: bag,hello,without,world
# Example 2: Input: 'python,java,c,cpp' -> Output: c,cpp,java,python

text = input("Enter comma-separated words: ")

words = [w.strip() for w in text.split(",")]
words.sort(key=str.lower)

print("Sorted words:", ",".join(words))

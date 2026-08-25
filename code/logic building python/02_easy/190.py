# Find all duplicate characters in a string.
# Example 1: Input: 'programming' -> Output: ['r', 'g', 'm']
# Example 2: Input: 'hello' -> Output: ['l']

text = input("Enter a string: ")

counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1

duplicates = [char for char, count in counts.items() if count > 1]
print("Duplicate characters:", duplicates)

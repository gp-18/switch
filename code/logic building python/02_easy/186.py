# Find all words in a list that are longer than k characters.
# Example 1: Input: words='apple banana cat', k=4 -> Output: ['apple', 'banana']
# Example 2: Input: words='hi hello hey', k=3 -> Output: ['hello']

words = input("Enter space-separated words: ").split()
k = int(input("Enter length k: "))

long_words = [word for word in words if len(word) > k]

print(f"Words longer than {k} characters:", long_words)

# Return indices of all capital letters in a string.
# Example 1: Input: 'eDaBiT' -> Output: [1, 3, 5]
# Example 2: Input: 'eQuINoX' -> Output: [1, 3, 4, 6]

text = input("Enter a string: ")

capital_indices = [i for i, char in enumerate(text) if char.isupper()]
print("Capital letter indices:", capital_indices)

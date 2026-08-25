# Reverse a string and swap its case.
# Example 1: Input: 'Hello World' -> Output: DLROw OLLEh
# Example 2: Input: 'Python 3' -> Output: 3 NOHTYp

text = input("Enter a string: ")

result = text[::-1].swapcase()
print("Reversed with swapped case:", result)

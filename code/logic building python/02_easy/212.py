# Unpack a list into first, middle, and last using destructuring.
# Example 1: Input: [1, 2, 3, 4, 5] -> Output: first=1, middle=[2, 3, 4], last=5
# Example 2: Input: ['a', 'b', 'c', 'd'] -> Output: first='a', middle=['b', 'c'], last='d'

numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers
print("List:", numbers)
print("First:", first)
print("Middle:", middle)
print("Last:", last)

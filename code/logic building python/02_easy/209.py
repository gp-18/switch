# Compute Hamming distance between two strings.
# Example 1: Input: str1='abcde', str2='bcdef' -> Output: 5
# Example 2: Input: str1='karolin', str2='kathrin' -> Output: 3

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2):
    distance = sum(c1 != c2 for c1, c2 in zip(str1, str2))
    print("Hamming distance:", distance)
else:
    print("Strings must be of equal length")

# Return a list from 1 to n amplifying multiples of 4 by 10.
# Example 1: Input: 4 -> Output: [1, 2, 3, 40]
# Example 2: Input: 8 -> Output: [1, 2, 3, 40, 5, 6, 7, 80]

n = int(input("Enter n: "))

if n >= 1:
    amplified = [i * 10 if i % 4 == 0 else i for i in range(1, n + 1)]
    print("Amplified list:", amplified)
else:
    print("Please enter a positive integer")

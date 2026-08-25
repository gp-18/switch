# Count occurrences of an element in a list.
# Example 1: Input: 1 2 2 3 3 3 -> Output: {1: 1, 2: 2, 3: 3}
# Example 2: Input: 5 5 5 -> Output: {5: 3}

array = list(map(int,input("Enter the numbers : ").split()))

freq = {}
for value in array : 
    if value in freq : 
        freq[value] += 1
    else : 
        freq[value] = 1

print(freq)

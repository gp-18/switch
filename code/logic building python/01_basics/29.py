# Find the sum of all elements in an array.
# Example 1: Input: 5 -> Output: 15
# Example 2: Input: 10 -> Output: 55

array = [100,200,300,400,500]
# print(sum(array))

answer = 0 
for i in range(len(array)) :
    print(i)
    answer = answer + array[i]

print(answer)

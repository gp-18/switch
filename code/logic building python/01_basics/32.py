# Find the minimum element in an array.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

array = [100,200,300,400.25,500.5]
print(min(array))

answer = float("inf") 

for i in range(len(array)) :
    if answer > array[i] :
        answer = array[i]

print(answer)

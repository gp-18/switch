# Find the average of array elements.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

array = [100,200,300,400.25,500.5]
print(sum(array)//len(array))

answer = 0 
for i in range(len(array)) :
    answer = answer + array[i]

print(answer//len(array))


# for value in array :

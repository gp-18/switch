# Find the average of array elements.

array = [100,200,300,400.25,500.5]
print(sum(array)//len(array))

answer = 0 
for i in range(len(array)) :
    answer = answer + array[i]

print(answer//len(array))


# for value in array : 
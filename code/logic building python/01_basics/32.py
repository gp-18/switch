# Find the minimum element in an array.

array = [100,200,300,400.25,500.5]
print(min(array))

answer = float("inf") 

for i in range(len(array)) :
    if answer > array[i] :
        answer = array[i]

print(answer)
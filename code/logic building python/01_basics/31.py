# Find the maximum element in an array.

array = [100,200,300,400.25,500.5]
print(max(array))

answer = float("-inf")

for i in range(len(array)) :

    if array[i] > answer : 
        answer = array[i]

print(answer)
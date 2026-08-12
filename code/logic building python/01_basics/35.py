# Find the index of the maximum element in an array.

array = [-100,0,200,0,1300,-140.25,-500.5]

max_value = 0
for i in range(len(array)) :
    if array[i] > array[max_value] : 
        max_value = i 


print(f"the index for the max value is {max_value}")
# Find the index of the minimum element in an array.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

array = [-100,0,200,0,1300,-140.25,-500.5]

min_value = 0 

for i in range(len(array)) :
    if array[i] < array[min_value] :
        min_value = i 

print(f"the index for the min value is {min_value}")

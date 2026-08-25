# Copy one array to another manually (without assignment).
# Example 1: Input: [10, 20, 30] -> Output: [10, 20, 30]
# Example 2: Input: ['a', 'b'] -> Output: ['a', 'b']

array = [-100,0,200,0,1300,-140.25,-500.5]
new_array = []
new_array_1 = array.copy()

print(new_array_1)

for value in array :
    new_array.append(value)

print(new_array)

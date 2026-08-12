# Copy one array to another manually (without assignment).

array = [-100,0,200,0,1300,-140.25,-500.5]
new_array = []
new_array_1 = array.copy()

print(new_array_1)

for value in array :
    new_array.append(value)

print(new_array)

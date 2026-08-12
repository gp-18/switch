# Count how many elements are positive, negative, or zero in an array.

array = [-100,0,200,0,1300,-140.25,-500.5]
postive = negative = zero = 0 

for i in range(len(array)) :
    if array[i] < 0 : 
        negative += 1 
    elif array[i] == 0 : 
        zero += 1 
    else : 
        postive += 1 

print(f"positve : {postive} , negative : {negative} & zero : {zero}")
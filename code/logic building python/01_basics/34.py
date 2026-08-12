# Count how many elements are even and odd in an array.

array = [-100,0,200,0,1300,-140.25,-500.5]

odd = even = 0 

for value in array : 
    if value % 2 == 0 : 
        even += 1 

    if value % 2 != 0 : 
        odd += 1 


print(f"odd : {odd} & even : {even}")

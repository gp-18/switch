# Count how many elements are even and odd in an array.
# Example 1: Input: 4 -> Output: the number is even
# Example 2: Input: 7 -> Output: the number is odd

array = [-100,0,200,0,1300,-140.25,-500.5]

odd = even = 0 

for value in array : 
    if value % 2 == 0 : 
        even += 1 

    if value % 2 != 0 : 
        odd += 1 


print(f"odd : {odd} & even : {even}")

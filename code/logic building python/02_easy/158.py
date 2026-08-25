# Count how many words in a sentence contain the letter 'a'.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (string := input("Enter the sentence: ")):

    total_count = 0 
    temp_count = 0 

    for char in string : 
        if temp_count == 0 and char.lower() == "a" :
            total_count +=1 
            temp_count = 1 

        if temp_count == 1 and char == " " :
            temp_count = 0 

    print(total_count)

else:
    print("Enter a valid sentence")

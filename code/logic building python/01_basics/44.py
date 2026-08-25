# Count how many spaces are in a sentence.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

sentence = str(input("Enter the sentence : ")).strip()

count = 0 
for value in sentence : 
    if value == " " :
        count += 1 


print(count)

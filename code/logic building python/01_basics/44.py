# Count how many spaces are in a sentence.

sentence = str(input("Enter the sentence : ")).strip()

count = 0 
for value in sentence : 
    if value == " " :
        count += 1 


print(count)
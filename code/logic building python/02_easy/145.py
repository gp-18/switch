# Count how many words in a sentence end with 's'.

if (string := input("Enter the string: ")) and len(string) >= 1:

   count = 0 
   for i in range(len(string)) :
       if (string[i] == "s" or string[i] =="S") :
           if i == len(string) - 1 or string[i + 1] == " ":
                count = count+1
   print(count)

else:
    print("Enter a valid string")
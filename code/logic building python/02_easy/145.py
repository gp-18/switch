# Count how many words in a sentence end with 's'.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (string := input("Enter the string: ")) and len(string) >= 1:

   count = 0 
   for i in range(len(string)) :
       if (string[i] == "s" or string[i] =="S") :
           if i == len(string) - 1 or string[i + 1] == " ":
                count = count+1
   print(count)

else:
    print("Enter a valid string")

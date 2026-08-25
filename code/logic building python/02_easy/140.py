# Print the ASCII value of each character in a string.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

if (string := str(input("Enter the string : "))) and len(string) >= 1 : 
    for char in string : 
        print(ord(char)) 
else : 
    print("Enter the correct thing")

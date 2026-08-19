# Print the ASCII value of each character in a string.

if (string := str(input("Enter the string : "))) and len(string) >= 1 : 
    for char in string : 
        print(ord(char)) 
else : 
    print("Enter the correct thing")
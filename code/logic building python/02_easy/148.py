# Check if two strings are the reverse of each other.

if (string1 := input("Enter the string: ")) and len(string1) >= 1  :
    if (string2 := input("Enter the string: ")) and len(string1) >= 1 :

        if len(string1)!= len(string2) :
            print("cannot be equal reversed") 

        is_equal = True

        for i in range(len(string1)) :
            if string1[i] != string2[len(string2)-1-i] :
                is_equal = False 
                break

        print("yes") if is_equal else print("No")
        
    else : 
        print("Enter the correct string2")
else : 
    print("Enter the correct string1")
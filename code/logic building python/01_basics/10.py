# Take a character and check whether it's uppercase, lowercase, a digit, or a special character.

character = input("Enter the character : ")

if character.isupper() :
    print("uppercase")
elif character.islower() :
    print("lowercase")
elif character.isdigit() :
    print("digit")
else : 
    print("special case")
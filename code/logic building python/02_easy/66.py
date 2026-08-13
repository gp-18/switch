# Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.

if ( number := int(input("Enter the number : "))) >= 0 : 
    if number % 100 == 0 and number % 500 == 0 and number % 2000 == 0 : 
        print("yes its evenly divided")
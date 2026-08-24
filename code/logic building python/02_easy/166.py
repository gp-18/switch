# Print frequency of each digit (0–9) in a given number.

if( number := int(input("Enter the number : "))) >= 1 : 
    freq = {}

    while number > 0 : 
        last_digit = number % 10

        if last_digit in freq : 
            freq[last_digit]+=1 
        else :
            freq[last_digit]=1

        number = number // 10

    print(freq)

else : 
    print("give correct number")
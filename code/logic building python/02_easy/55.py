# Take marks (0–100) and print the corresponding grade (A/B/C/D/F).

marks = int(input("Enter the marks : "))

if 0 <= marks <= 33 : 
    print("F")
elif 34 <= marks <= 44 :
    print("E")
elif 45 <= marks <= 55 : 
    print("D")
elif 56 <= marks <= 66 : 
    print("C")
elif 67 <= marks <= 77 : 
    print("B")
elif 78 <= marks <= 100 : 
    print("A")
else : 
    print("Enter the correct marks")
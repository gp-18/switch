# Take income and age, and check if eligible for tax (age > 18 and income > 5L).
if (age := int(input("Enter the age: "))) >= 0 and (income := int(input("Enter the income: "))) >= 0:
    if age > 18 and income > 500000:
        print("Yes, eligible for tax")
    else:
        print("No, not eligible for tax")
else:
    print("Enter valid values")
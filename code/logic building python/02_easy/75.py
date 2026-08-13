# Calculate electricity bill based on units consumed.

units = int(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units")

elif units <= 100:
    bill = units * 5
    print("Electricity bill:", bill)

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    print("Electricity bill:", bill)

elif units <= 400:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    print("Electricity bill:", bill)

else:
    bill = (100 * 5) + (100 * 7) + (200 * 10) + ((units - 400) * 15)
    print("Electricity bill:", bill)
# Take coordinates (x, y) and determine which quadrant the point lies in.

x = int(input("Enter the x coordinate: "))
y = int(input("Enter the y coordinate: "))

if x == 0 and y == 0:
    print("Lies in the origin")

elif y == 0 and x > 0:
    print("Lies on the positive x-axis")

elif y == 0 and x < 0:
    print("Lies on the negative x-axis")

elif x == 0 and y > 0:
    print("Lies on the positive y-axis")

elif x == 0 and y < 0:
    print("Lies on the negative y-axis")

elif x > 0 and y > 0:
    print("Lies in the 1st quadrant")

elif x < 0 and y > 0:
    print("Lies in the 2nd quadrant")

elif x < 0 and y < 0:
    print("Lies in the 3rd quadrant")

elif x > 0 and y < 0:
    print("Lies in the 4th quadrant")
# Take two angles of a triangle and compute the third angle.

if (angle1 := int(input("Enter the angle 1: "))) > 0 and (angle2 := int(input("Enter the angle 2: "))) > 0:
    if angle1 + angle2 >= 180:
        print("This is not possible")
    else:
        print(180 - (angle1 + angle2))
else:
    print("Angles must be greater than 0")
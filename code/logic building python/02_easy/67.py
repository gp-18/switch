# Take two angles of a triangle and compute the third angle.
# Example 1: Input: 3, 4, 5 -> Output: Valid triangle
# Example 2: Input: 1, 2, 10 -> Output: Invalid triangle

if (angle1 := int(input("Enter the angle 1: "))) > 0 and (angle2 := int(input("Enter the angle 2: "))) > 0:
    if angle1 + angle2 >= 180:
        print("This is not possible")
    else:
        print(180 - (angle1 + angle2))
else:
    print("Angles must be greater than 0")

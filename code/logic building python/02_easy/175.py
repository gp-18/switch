# Calculate Body Mass Index (BMI) given height and weight.
# Example 1: Input: 5 -> Output: Sample Output 1
# Example 2: Input: 10 -> Output: Sample Output 2

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

if weight > 0 and height > 0:

    bmi = weight / (height * height)

    print("BMI:", round(bmi, 2))

    if bmi < 18.5:
        print("Underweight")

    elif bmi < 25:
        print("Normal weight")

    elif bmi < 30:
        print("Overweight")

    else:
        print("Obesity")

else:
    print("Enter valid height and weight")

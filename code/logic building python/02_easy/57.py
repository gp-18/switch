# Take the hour of the day (0–23) and print 'Good Morning', 'Good Afternoon', 'Good Evening', or 'Good Night'.
hour = int(input("Enter the hour (0-23): "))

if 0 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 17:
    print("Good Afternoon")
elif 17 <= hour < 21:
    print("Good Evening")
elif 21 <= hour <= 23:
    print("Good Night")
else:
    print("Invalid hour. Please enter a value between 0 and 23.")
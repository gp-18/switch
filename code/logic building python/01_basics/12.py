# Take a day number (1–7) and print the corresponding day name.


def check_day(number : int = 1 ) :
    days  = {
        1 : "monday" ,
        2 : "tuesday" ,
        3 : "wednesday" ,
        4 : "thursday" ,
        5 : "friday" ,
        6 : "saturday" ,
        7 : "sunday"
    }

    return days.get(number , "enter the valid number to get the day")



number = int(input("give me the number : "))
print(check_day(number=number))
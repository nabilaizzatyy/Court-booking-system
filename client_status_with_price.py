# import module of greetings opening
from display_sentence import greetings_opening
greetings_opening()

# import module of court number to get input from the user
from Court_user_input import court_number


#to determine it is a UNITEN Student or Public
client_status = str(input("\nAre you UNITEN Student? (Type Yes or No):"))

#import module of day & hours , to get input of day & hours from user
from dayNhours import booking_day , booking_hours


if client_status.lower()== "yes":
    status = "UNITEN Student"
    if court_number == 1:
        price = 50
            
    elif court_number == 2:
        # price on monday to friday is different from saturday to sunday
        if booking_day.lower() not in ("saturday","sunday"):
            price = 20
        else:
            price = 25
            
    elif court_number == 3:
        price =55
    
    elif court_number == 4:
        if booking_day.lower() not in ("saturday","sunday"):
            price = 30
        else:
            price = 35

# for the public because UNITEN Student price and Public are different
elif client_status.lower()=="no":
    status = "Public User"
    
    if court_number == 1:
        if booking_day.lower() not in ("saturday","sunday"):
            price = 60
        else:
            price = 80
            
    elif court_number == 2:
        if booking_day.lower() not in ("saturday","sunday"):
            price = 60
        else:
            price = 65
            
    elif court_number ==3:
        if booking_day.lower() not in ("saturday","sunday"):
            price = 65
        else:
            price = 85
    
    elif court_number == 4:
        if booking_day.lower() not in ("saturday","sunday"):
            price = 60
        else:
            price = 65

#calculations for payment
total_price = price * booking_hours

#details to show for the user
print ("\nRental Details")
print (f"Court:{court_number}")
print (f"UNITEN Student : {client_status}")
print (f"Day:{booking_day}")
print (f"Hours:{booking_hours}")
print (f"Total amount you need to pay: RM{total_price}")
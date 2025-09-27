#To avoid error when user enter the invalid input
while True:
    court_number = int(input("\nPlease select the court you would like to book by inserting the relevant number:"))
    if court_number == 1:
        print("You inserted number 1, Futsal")
        break
    
    elif court_number == 2:
        print("You inserted number 2, Sepak Takraw")
        break
    
    elif court_number == 3:
        print("You inserted number 3, Basketball")
        break
    
    elif court_number == 4:
        print("You inserted number 4, Badminton")
        break
    
    else:
        print("Invalid number. Please try again")
from client_status_with_price import total_price
from display_sentence import greetings_closing

while True:
    payment = int(input("\nPlease insert amount of payment(RM 1 , RM5, RM10, RM50 or RM100):RM"))
    if payment in (1,5,10,50,100):
        balance = total_price - payment
        total_price = balance
        
        if balance > 0:
            print("\nRemaining balance is RM", balance)
            
            
        elif balance ==0:
            greetings_closing()
            break
        
        
        elif balance < 0:
            balance = -total_price
            print ("\nThe balance is RM",balance)
            greetings_closing()
            break
    else:
        print("Reminder: Please enter RM1, RM5, RM10, RM50 or RM100 only")
        
end = input("\nPlease click 'enter' to exit")
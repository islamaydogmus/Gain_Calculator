# Gain Calculator
Calculates the gain of your investment (just EUR/TRY for now) by sending a notification.

'setting.json' has 3 parameters:  
• "PORTF": Your current savings in Euro.  
• "EUR_BOUGH": Euro/TRY ratio when you bought it.  
• "FEE": The amount received by the bank for transaction. 
This values will be read by the program everytime you run it so it has to be in the same location with the 'main.py'
 
Output will be 4 values as form of;

    Euro Currently: {current_EUR} TL  
    Net change in Euro is {rise}  
    Your gain(loss) without fee : {gain} TL  
    Your net gain(loss) is: {round(gain - FEE,4)} TL  



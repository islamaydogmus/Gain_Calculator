from get_EURTRY import get_EURTRY
from win10toast import ToastNotifier
import json

def calc_net_gain():
    """
    This function calculates your gain in terms of TRY by values that you set 
    in "settings.json" and the live EURO values that https://www.bloomberght.com
    provides.
    PORTF: Your current savings in Euro.
    EUR_BOUGHT: Euro/TRY ratio when you bought it. 
    FEE: The amount received by the bank for transaction.
    """

    # Reading the 'settings.json'
    with open("settings.json","r") as file:
        settings = json.load(file)
    
    # Setting the variables after reading 'settings.json'
    PORTF = settings["PORTF"]
    EUR_BOUGHT = settings["EUR_BOUGH"]
    FEE = settings["FEE"]
    current_EUR = get_EURTRY()


    # Calculation of gain
    rise = round(current_EUR - EUR_BOUGHT,4)
    gain = round(rise * PORTF,4)
    
    # Display
    content = f"""
    Euro Currently: {current_EUR} TL
    Net change in Euro is {rise}
    Your gain(loss) without fee : {gain} TL
    Your net gain(loss) is: {round(gain - FEE,4)} TL
    """
    return content

# Poping a windows notification
favicon_loc = "Eur.ico"
toaster = ToastNotifier()
toaster.show_toast(title="EUR/TR",msg=calc_net_gain(),
    duration=20,
    icon_path=favicon_loc)
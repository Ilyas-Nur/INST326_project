import datetime     ##imported for holiday_szn method

def holiday_szn():
    """

        This method determines whether the current day we're in is close to a holiday

        If the day is past or on the 15th of the month of November, its Thanksgiving season
        
        If the day is past or on the 15th of the month of December, its Christmas season
        
        If the day is before or on the 15th of the month of January, its New Year's season
        
        If not, returns None (Falsy)
        
        Args:
            x (optionl):A date if you would actually like to specify. Could be handy if you
            are planning to buy a car that dar
        
        Returns:
            True or False: Depending on the currrent day and month
        
        By. Ilyas Nur
        
    """
    x = datetime.datetime.now()
    
    if x.strftime("%B") == "November":
        if int(x.strftime("%d")) >= 15:
            print("It's almost Turkey day! Here's a discount")
            return True
        else:
            print("Its not the holidays, so unfortuntely no discount")
        
    elif x.strftime("%B") == "December":
        if int(x.strftime("%d")) >= 15:
            print("It's almost Christmas. Your present is a discount!")
            return True
        else:
            print("Its not the holidays just yet!, so unfortuntely no discount")
        
    elif x.strftime("%B") == "January":
        if int(x.strftime("%d")) <= 15:
            print("We are still in the holiday spirit from the New Year, have a discount!")
            return True
        else:
            print("Its not the holidays anymore, so unfortuntely no discount")
        
    elif x.strftime("%B") != "November" and x.strftime("%B") != "December" and x.strftime("%B") != "January":
        print("Its not the holidays, so unfortuntely no discount")
        return False
    
print(holiday_szn())
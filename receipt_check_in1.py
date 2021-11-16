def receipt():
    """
    The method produces a receipt of all cost associated with the
     purchase of a vehicle. The method includes the multiple costs that come,
     including price of car, fees etc.
     
     Args:
     costbreak(list): The titles of the costs associated with the purchase
     prices(list): The broken down costs by dollar amount
     total(list): a new list, a combination of costbreak and prices using (zip)
     
     Returns:
     A receipt of the costs broken down including a count of each payment portion
    """
    costbreak = ["Car payment:","Dealer payement:","Salesperson cut:","Servicing fee:"]
    prices = ["50,000","$400","$70","$35"]
    total = zip(costbreak,prices)
    for i,(costbreak,prices) in enumerate(total):
        print(i,costbreak,prices)
        
print(receipt())
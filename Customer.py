class Customer:
    """
        This class enables us to create customer objects who will purchase a
        vehicle.
        
        Attributes:
            name (str): Name of the customer
            age (int): Age of customer
            income (int): Annual income of customer
            credit_score (int): The credit score of the customer
            driving_record (bool): Whether customer has been in previous car
                accident
            owned_cars (list of Vehicle): list of Vehicle objects (cars) the
                customer owns
            
    """
    def __init__(self, name, age, income, credit_score, driving_record):
        """Initializes Customer class.
        
        Args:
            See Customer class documentation.
        """
        self.income = int(income)
        self.age = int(age)
        self.name = name
        self.credit_score = int(credit_score)
        self.driving_record = driving_record
        self.owned_cars = []
        
    def monthly_payment (self, price):
        """Calculates the montly payment including interest based on customer
            attributes.
            
            Args:
                price (int): price the vehicle was purchased for
            
            Returns:
                float: specific monthly payment including interest of the car 
                    for the customer over a 72 month payment period
        """
        
        points = 0
        
        if (self.income*.35)< price:
            points +=1
        if self.credit_score < 700:
            points +=1
        if len(self.driving_record) > 0:
            points +=1
        if self.age < 25:
            points +=1
            
        #payment per month
        ppm = round(price//72)
        
        interestpayment = price * .05 * points
        
        #interest payment per month
        ippm = interestpayment//72
        
        #monthly payment + interest
        return ppm + ippm
class Customer:
    """
        This class enables us to create customer objects who will purchase a
        vehicle.
        
        Attributes:
            name (str): The name of the customer
            credit_score (int): The credit score of the customer
            in_college (bool): True if customer is enrolled in college, False
            otherwise.
            previous_accident (bool): List of previous accidents drivers been in
            
    """
    def __init__(self, name, age, income, credit_score, driving_record):
        self.income = int(income)
        self.age = int(age)
        self.name = name
        self.credit_score = int(credit_score)
        self.driving_record = driving_record
        self.points = 0
        self.owned_cars = []
        
    def monthly_payment (self, price):
        #Calculate the loan term based on the attributes they carry
        if (self.income*.35)< price:
            self.points +=1
        if self.credit_score < 700:
            self.points +=1
        if len(self.driving_record) > 0:
            self.points +=1
        if self.age < 25:
            self.points +=1
            
        #payment per month
        ppm = round(price//72)
        
        interestpayment = price * .05 * self.points
        
        ippm = interestpayment//72
        
        return ppm + ippm
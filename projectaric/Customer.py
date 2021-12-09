class Customer:
    """
        This class enables us to create customer objects who will purchase a
        vehicle.
        
        Attributes:
            name (str): The name of the customer
            credit_score (int): The credit score of the cusotmer
            in_college (bool): True if customer is enrolled in college, False
            otherwise.
            previous_accident (bool): List of previous accidents drivers been in
            
    """
    def __init__(self, name, credit_score, in_college, previous_accident):
        self.name = name
        self.credit_score = credit_score
        self.in_college = in_college
        self.previous_accident = previous_accident
        self.owned_cars = []
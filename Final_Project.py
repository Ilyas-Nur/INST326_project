"""A simple ......."""

#thomas made an edit

"""The Packers play thursday night"""

#ilyas made an edit

"""The Ravens lost to the Bengals"""
#Jose made an edit

import re
import math

class Dealership:
    """
        This class creates a dealership from vehicles. Can offer specific specials
        and deals for customers. 

        Attributes:
            - name (str): name of dealership
            - inventory (int): The amount of cars that are in the dealership
            - showroom (list): List of cars currently for sale
            - general_apr (int): General interest rate charged to customers
            - holiday_szn (bool): optional only when its the holidays. Subtracts
            $1,000 from vehicle MSRP.   
    """
    pass

class Vehicle(Dealership):
    """
        This class enables us to create vehicle objects
        
         Attributes:
            - year (str): Year of vehicle
            - make (str): Make of vehicle
            - model (str): Model of vehicle
            - type (str): Type of vehicle (sedan, hatchback, truck, SUV, van, coupe)
            - fuel_type (str): The type of fuel the vehicle takes
            - msrp (int): The price of the vehicle
            - adj_price: Revised price based on positive customer attributes
            
    """
    ## We can override general delearship interest rate in this class when customer has credit score
    #above 700
    
    def __init__(self, vehicle_info):
        """
            Takes a single line of text as an argument when instatiating the class
            and sets the attributes.
            
            Args:
                - vehicle_info (str): a single line of text (this line is the
                entire vehicle info)
            
            Side effects:
                - Sets attributes to every object instatiated from the class
                
            Raises:
                ValueError: Indicates when the vehicle_info string could not be parsed
        """
        
        regex = """
        
        
        
        """
        
        #if re.search(regex, vehicle_info):
            # match = re.search(regex, vehicle_info)
            # self.year = match.group("year")
            # self.make = match.group("make")
            # self.model = match.group("model")
            # self.type = match.group("type")
            # self.fuel_type = match.group("fuel_type")
            # self.msrp = match.group("msrp")
            # self.adj_price = match.group("adj_price")
            #
        #else:
            #raise ValueError
        
    ##[dealershipname].showroom.append(basic_car_info) ##To add to the delarship 
    # #### Above is IMPORTANT!!!
    
    ##basic_car_info will be a focus group that gets the year, make and model cause 
    # we want just basic info in the showroom
        
def read_vehicles(filename, file2 = "", file3 = ""):
    """
        Could read vehicles form up to three files, after that the dealership
        would be full.
        
        Args:
            - filename (str): A path to a file containing one vehicle per line
            - file2 (str): An OPTIONAL path to a file containing one vehicle per line
            - file3 (str): An OPTIONAL path to a file containing one vehicle per line
            
        Side effects:
            - Every object will be stored in the list "list_vehicles"
            
        Returns:
            - vehicles (list): A list of one instance of 'Vehicle' per line in the
            file. (Store this in dealership 'showroom' attribute)
            
            
        
    """
    
class Customer(Vehicle):
    """
        This class enables us to create customer objects who will purchase a
        vehicle.
        
        Attributes:
            name (str): The name of the customer
            age (int): The age of the customer
            credit_score (int): The credit score of the cusotmer
            college_student (bool): True if customer is enrolled in college, False
            otherwise.
            driving_record (list): List of previous accidents drivers been in
            
    """
    pass
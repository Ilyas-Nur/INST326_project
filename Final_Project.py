import re
import math
import datetime

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
    
    def __init__(self, name, general_apr, car_shipment):
        self.name = name
        self.general_apr = general_apr
        self.car_shipment = car_shipment
        
        with open(self.car_shipment, "r", encoding = "utf-8") as f:
            list_vehicles = [Vehicle(line) for line in f]
            self.car_shipment = list_vehicles

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
            
        """
        x = datetime.datetime.now()
        
        if x.strftime("%B") == "November":
            if int(x.strftime("%d")) >= 13:
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
        


class Vehicle(Dealership):
    """
        This class enables us to create vehicle objects
        
         Attributes:
            - year (str): Year of vehicle
            - make (str): Make of vehicle
            - owner (str): Owner of vehicle
            - title
            - model (str): Model of vehicle
            - type (str): Type of vehicle (sedan, hatchback, truck, SUV, van, coupe)
            - fuel_type (str): The type of fuel the vehicle takes
            - msrp (int): The price of the vehicle
            - purchase_history (list)
            - adj_price: Revised price based on positive customer attributes
            
    """
   
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
        (?x)
        ^
        (?P<Car_Name>(?P<Year>\d{4})
        \s
        (?P<Make>\S+)
        \s
        (?P<Model>[^,]+)),
        \s
        ((?P<Car_Type>\([^,]+),)?
        (?P<Fuel_Type>[^,]+)?,
        \s
        (?P<MSRP>\$\S+)?
        """
        
        if re.search(regex, vehicle_info):
            match = re.search(regex, vehicle_info)
            
            self.car_name = match.group("Car_Name") # Captures Year, Make, and Model
            self.year = match.group("Year") # Captures year of vehicle
            self.make = match.group("Make") # Captures make of vehicle
            self.model = match.group("Model") # Captures model of vehicle
            self.type = match.group("Car_Type") # Captures car type (Sedan, SUV) if vehicles specify
            self.fuel_type = match.group("Fuel_Type") # Captures the fuel type of vehicle
            self.msrp = match.group("MSRP") # Captures the MSRP of vehicle
            
        else:
            raise ValueError ##
        
        

            
            
class Customer:
    """
        This class enables us to create customer objects who will purchase a
        vehicle.
        
        Attributes:
            name (str): The name of the customer
            age (int): The age of the customer
            owned_vehicles (list)
            credit_score (int): The credit score of the cusotmer
            college_student (bool): True if customer is enrolled in college, False
            otherwise.
            driving_record (list): List of previous accidents drivers been in        
    """
    
    pass
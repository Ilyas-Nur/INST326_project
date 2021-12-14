import re

class Vehicle:
    """
        This class enables us to create vehicle objects
        
         Attributes:
            - car_name (str): Full car name in the form "year make model"
            - year (str): Year of vehicle
            - make (str): Make of vehicle
            - model (str): Model of vehicle
            - type (str): Type of vehicle (sedan, hatchback, truck, SUV, van, coupe)
            - fuel_type (str): The type of fuel the vehicle takes
            - msrp (int): The price of the vehicle
    """
   
    def __init__(self, vehicle_info):
        """
            Takes a single line of text as an argument when instantiating the class
            and sets the attributes.
            
            Args:
                - vehicle_info (str): a single line of text (this line is the
                entire vehicle info)
            
            Side effects:
                - Sets attributes to every object instantiated from the class
                
            Raises:
                ValueError: Indicates when the vehicle_info string could not be parsed
        """
        
        regex = r"""
        (?x)
        ^
        (?P<Car_Name>(?P<Year>\d{4})
        \s
        (?P<Make>\S+)
        \s
        (?P<Model>[^,]+)),
        \s
        ((?P<Car_Type>\([^,]+),)?
        \s?
        (?P<Fuel_Type>[^,]+)?,
        \s
        (?P<MSRP>\$\S+)?
        """
        
        if re.search(regex, vehicle_info):
            match = re.search(regex, vehicle_info)
            
            self.car_name = match.group("Car_Name") # Captures Year, Make, and Model
            self.year = int(match.group("Year")) # Captures year of vehicle
            self.make = match.group("Make") # Captures make of vehicle
            self.model = match.group("Model") # Captures model of vehicle
            self.type = match.group("Car_Type") # Captures car type (Sedan, SUV) if vehicles specify
            self.fuel_type = match.group("Fuel_Type") # Captures the fuel type of vehicle
            self.msrp = int(match.group("MSRP")[1:]) # Captures the MSRP of vehicle
            
        else:
            raise ValueError("Error in import")
        
    
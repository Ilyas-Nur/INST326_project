import datetime
from Vehicle import Vehicle

class Dealership:
    """
        This class creates a dealership from vehicles. Can offer specific specials
        and deals for customers. 

        Attributes:
            - name (str): name of dealership
            - showroom (list): List of cars currently for sale
            - general_apr (int): General interest rate charged to customers
            - car_shipment ..
    """
    def __init__(self, general_apr, car_shipment):
    
        self.general_apr = general_apr
        self.car_shipment = car_shipment
        self.showroom = []
        
        with open(self.car_shipment, "r", encoding = "utf-8") as f:
            self.showroom = [Vehicle(line) for line in f]
    
    def check_holiday(self):
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
            if int(x.strftime("%d")) >= 13:
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
    
    def sell(self, fullname):
        for car in self.showroom:
            if str(car.car_name) == str(fullname):
                self.showroom.remove(car)
                return car
   
    def display(self, list):
        if len(list) == 0:
            for car in self.showroom:
                print(f"{car.year} {car.make} {car.model}")
        else:
            for car in list:
                print(f"{car.year} {car.make} {car.model}")
    
    def display_charts(self):
        #thomas code for seaborn plots
        pass

    def calculate_msrp(self, vehicle):
        if self.check_holiday() == True:
            return vehicle.msrp- 1_000
        return vehicle.msrp
    
    def print_receipt(self, cstmer):
        with open("receipt.txt", "w", encoding = "utf-8") as f:#output as pdf maybe
            for car in cstmer.owned_cars:
                f.write(f"Monthly Payment:  {cstmer.monthly_payment(car)}\n")
                f.write(f"Customer Name:  {cstmer.name}\n")
                f.write(f"Car Purchased:  {car.year} {car.make} {car.model}\n")
                f.write(f"Time of Purchase: ")#out put time of purchase
                #f.write()#default msrp, then deductions one by one, dashed line across, total price, followed by double newline space

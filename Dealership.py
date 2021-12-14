import datetime
from datetime import date

from Vehicle import Vehicle
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


class Dealership:
    """
        This class creates a dealership from vehicles. Can offer specific
        specials and deals for customers. 

        Attributes:
            - showroom (list): List of vehicle objects: cars currently for sale
            - car_shipment (str): filepath to car shipment text file
    """
    def __init__(self, car_shipment):
        """
            Requires an APR and a car shipment when instatiating the class. Assigns 
            attributes.
            Side effects:
                - Instantiates Vehicle objects
                - Appends those objects to self.showroom
        """
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
                are planning to buy a car that day
            
            Returns:
                True or False: Depending on the currrent day and month
            
        """
        x = datetime.datetime.now()
        
        if x.strftime("%B") == "November":
            if int(x.strftime("%d")) >= 13:
                return True
            else:
                return False
        elif x.strftime("%B") == "December":
            if int(x.strftime("%d")) >= 15:
                return True
            else:
                return False
        elif x.strftime("%B") == "January":
            if int(x.strftime("%d")) <= 15:
                return True
            else:
                return False
    
    
    def sell(self, fullname):
        """Sell a car from the dealership to a customer.
        Args:
            fullname (str): full name of the car (year make model)
        
        Returns:
            (Vehicle): located car object from dealership list of vehicles
        """
        for car in self.showroom:
            if car.car_name == fullname:
                self.showroom.remove(car)
                return car
   
    def display(self, filtered_list):
        """Displays a list of all the cars in the dealership.
        Args:
            filtered_list (list of Vehicle): list of all vehicles that fit the specified filters
        
        Side effects:
            Prints the full name of the each car in the dealership
        """
        if len(filtered_list) == 0:
            for car in self.showroom:
                print(f"{car.car_name}")
        else:
            for car in filtered_list:
                print(f"{car.car_name}")
    
    def display_chart(self):
        """Displays the car dealership data into several useful visual plots.
        
        Side effects:
            Displays seaborn plot.
        """
        plt.figure(figsize=(13,8))
        
        makes = []
        msrps = []
        for car in self.showroom:
            makes.append(car.make)
            msrps.append(car.msrp)
        
        df = pd.DataFrame()
        df['Make'] = makes
        df['MSRP'] = msrps
        
        grouped = df.groupby('Make', as_index=False)['MSRP'].mean()
        
        sns.barplot(x=grouped.Make, y=grouped.MSRP).set(xlabel = "Make", \
            ylabel= "Average MSRP", title='Barplot of Average MSRP per Make')
        
        plt.xticks(
            rotation=45, 
            horizontalalignment='right',
            fontsize='x-large',
            fontweight='light'
        )
        
        plt.show()

    def calculate_msrp(self, vehicle):
        """Calculates potential discounted MSRP based on holiday season.
        Args:
            vehicle (Vehicle): vehicle being checkied for a holiday discount
        """
        if self.check_holiday() == True:
            return vehicle.msrp - 1_000
        return vehicle.msrp
    
    def print_receipt(self, customer):
        """Creates txt file receipt after vehicle purchases car(s).
        Args:
            customer (Customer): customer who bought the cars
            
        Side effects:
            Creates receipt txt file and writes information including customer 
            attributes to the file.
        """
        day = date.today().strftime("%m/%d/%y")
        with open("receipt.txt", "w", encoding = "utf-8") as f:
            f.write("CAR PURCHASE RECEIPT\n")
            f.write("---------------------------------\n")
            f.write(f"Date of Purchase: {day}\n")
            f.write(f"Customer Name: {customer.name}\n")
            f.write(f"Customer Age: {customer.age}\n")
            f.write(f"Customer Income: ${customer.income}\n")
            for car in customer.owned_cars:
                f.write(f"\nCar Purchased: {car.year} {car.make} {car.model}\n")
                f.write(f"Default MSRP: ${car.msrp}\n")
                if(self.check_holiday()):
                    f.write("It's a holiday season!\n")
                    f.write(f"Holiday Price Reduction: -$1000\n")
                    f.write(f"Final Total MSRP: ${self.calculate_msrp(car)}\n")
                f.write(f"Calculated Monthly Payment Required + Interest:  ${customer.monthly_payment(self.calculate_msrp(car))}\n")
            f.write("\nThank you for your purchase!")
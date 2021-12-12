import datetime
from datetime import date
from Vehicle import Vehicle
import seaborn as sns
import matplotlib.pyplot as plt


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
                return True
            else:
                return False
        elif x.strftime("%B") == "December":
            if int(x.strftime("%d")) >= 10:
                return True
            else:
                return False
        elif x.strftime("%B") == "January":
            if int(x.strftime("%d")) <= 15:
                return True
            else:
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
        """Displays the car dealership data into several useful visual plots.
        Args:
            filepath (string): path to data file. (will eventually need, used 
                sample data from seaborn so I didn't use arg yet)
        Side effects:
            Displays seaborn and matplotlib plots.
        """
    
        sns.set_theme()
        sns.set(rc={'figure.figsize':(8,8)})
        sns.color_palette('pastel')[0:5]

    
        cars = sns.load_dataset('mpg').dropna()

    
        cars['brand'] = cars['name'].str.extract(r"(^\w+)", expand=True)
        pie_data = cars['brand'].value_counts()
    
        count = 0
        for i in list(pie_data.keys()):
            if pie_data[i] < 10:
                count +=1
                del pie_data[i]
        pie_data['other'] = count

        pie_label = pie_data.keys()
        
        sns.boxplot(x=cars.horsepower).set(xlabel = "Horsepower", title='Boxplot of Vehicle Horsepower')
        sns.barplot(x=cars.horsepower).set(xlabel = "Horsepower", title='Boxplot of Vehicle Horsepower')

        #bar chart of average price of vehicle for each brand

        plt.show()

    def calculate_msrp(self, vehicle):
        if self.check_holiday() == True:
            return vehicle.msrp - 1_000
        return vehicle.msrp
    
    def print_receipt(self, cstmer):
        day = date.today().strftime("%m/%d/%y")
        with open("receipt.txt", "w", encoding = "utf-8") as f:
            f.write("CAR PURCHASE RECEIPT\n")
            f.write("---------------------------------\n")
            f.write(f"Date of Purchase: {day}\n")
            for car in cstmer.owned_cars:
                f.write(f"Customer Name: {cstmer.name}\n")
                f.write(f"Car Purchased: {car.year} {car.make} {car.model}\n")
                f.write(f"Default MSRP: ${car.msrp}\n")
                if(self.check_holiday()):
                    f.write(f"Holiday Price Reduction: -$1000\n")
                    f.write(f"Final Total MSRP: ${self.calculate_msrp(car)}\n")
                f.write(f"Calculated Monthly Payment Required + Interest:  {cstmer.monthly_payment(self.calculate_msrp(car))}\n")
            f.write("\nThank you for your purchase!")
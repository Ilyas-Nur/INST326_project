from Dealership import Dealership
from Customer import Customer
import colorama
from colorama import Fore, Style
import sys
from argparse import ArgumentParser


def questionnaire(car_list):
    """
        Asks a questionaire for a customer to purchase a vehicle if customer
        unsure of what car to get.
        
        Args:
            car_list (list): List of vehicle objects
        
        Side effects:
            - Makes user input lowercase
            - Appending to filtered list
            - Prints messages based off user input
            
        Returns:
            adjusted_list (list): List of cars that fit the budget of the customer
    """
    filtered_list = []
    desires_eco = input(Fore.LIGHTBLUE_EX + "Do you want an eco-friendly car (y/n)? :: "+ Fore.WHITE).lower()
    if desires_eco == "n":
        for car in car_list:
            if car.fuel_type == "Gas":
                filtered_list.append(car)
        i=1
    else:
        for car in car_list:
            if car.fuel_type != "Gas":
                filtered_list.append(car)
    adjusted_list = []
    l = 0
    while l == 0:
        i= True
        while i:
            try:
                price_range = int(input(Fore.LIGHTBLUE_EX + "What is the most you want to spend on the car? :: "+ Fore.WHITE))
                i=False
            except ValueError:
                print("That is not a valid input")
            
        if price_range < 15000:
            print("Price is too low")
        else:
            for car in filtered_list:
                if car.msrp <= price_range:
                    adjusted_list.append(car)
            l=1
    return adjusted_list


def main(filepath):
    """Create dealership program that can be run in the command line.
    
        Args:
            filepath (str): path to car shipment text file.
        
        Side effects:
            Instantiates dealership class.
            Instantiates customer class.
            Displays seaborn plot.
            Prints text to command line.
            Ask for user input.
        
        Colorama Citation:  
            The colorama library (under BSD license) was used in order to add 
            color to the text in the commmand prompt. The creator was Jonathan 
            Hartley. 
            Python. (n.d.). Colorama. PyPI. Retrieved December 14, 2021, 
            from https://pypi.org/project/colorama/ 

    """
    colorama.init(autoreset=True)
    dealership = Dealership(filepath)
    print(Fore.RED + Style.BRIGHT + "Welcome to the Dealership!")

    print("Please fill in the customer information below.\n")
    name = input(Fore.LIGHTBLUE_EX + "What is your name? :: " + Fore.WHITE)
    age = input(Fore.LIGHTBLUE_EX + "What is your age? (enter integer) :: " + Fore.WHITE)
    income = input(Fore.LIGHTBLUE_EX + "What is your annual income? (enter integer) :: " + Fore.WHITE)
    score = input(Fore.LIGHTBLUE_EX + "Enter your credit score (300-850) :: " + Fore.WHITE)
    record = input(Fore.LIGHTBLUE_EX + "Have you been in any car accidents before? (y/n) :: " + Fore.WHITE)

    customer = Customer(name, age, income, score, record)
    
    print(Fore.RESET + "\nThank you for entering your information! It will be used to help calculate the price of your purchase and your interest rates!")
    user_input = input(Fore.MAGENTA + "\nWould you like to view a visual breakdown of the dealership (y/n)? :: " + Fore.WHITE)
    if (user_input == "y"):
        dealership.display_chart()
    running = True
    while(running):
        print(Fore.GREEN + "\nA car will now be purchased.\n")
        user_input = input(Fore.MAGENTA + "Do you need help deciding the type of car you want? :: " + Fore.WHITE)
        if(user_input == "y"):
            filtered_list = questionnaire(dealership.showroom)
            print(Fore.GREEN + "\nHere are all the cars offered.\n")
            dealership.display(filtered_list)
        else:
            print(Fore.GREEN + "\nHere are all the cars offered.\n")
            dealership.display(dealership.showroom)
    
            car_name = input(Fore.LIGHTYELLOW_EX + "\nEnter the name of the desired car :: " + Fore.WHITE)
        
        customer.owned_cars.append(dealership.sell(car_name))
        user_input = input(Fore.LIGHTMAGENTA_EX + "\nWould you like to buy another vehicle? (y/n) :: " + Fore.WHITE)
        if(user_input == "y"):
            pass
        else:
            running=False
    
    print(Fore.RESET + Fore.RED + "\nYou bought:")
    total_cost = 0
    for car in customer.owned_cars:
        total_cost += int(dealership.calculate_msrp(car))
        print(f"x1 {car.car_name}")
    print(f"The total payment due is: ${total_cost}")
    print("For full information about your purchase, review your receipt.")
    dealership.print_receipt(customer)
    
def parse_args(argList):
    """Parse command-line arguments.
    
    Expect one mandatory argument:
        -filepath: a path to the car shipment file
    
    Args:
        argList (list of str): arguments from the command line
    
    Returns:
        namespace: the parsed arguments, as a namespace
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help="filepath of shipment file")
    return parser.parse_args(argList)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath)
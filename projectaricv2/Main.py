from Dealership import Dealership
from Customer import Customer
import colorama
from colorama import Fore, Style


def questionnaire(car_list):
    """This class filters the showroom list from the Dealership file
    Args:
        car_list(list of strings): This is the list showroom from the Dealership file
    Returns:
        The method returns a filtered list dependant on the users inputs
    Raises:
        ValueError: If the input given isn't a number, a value error is raised
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
    price_list = []
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
                if car.msrp < price_range:
                    price_list.append(car)
            l=1
    return price_list
        


def console_displayer():
    """This method creates a user interface, which provides user inputs to show filtered list
    based on user defined criteria
    Side effects:
    prints the filtered list from the questionnaire method 
    """
    colorama.init(autoreset=True)
    dealership = Dealership(0.8, "car_shipment2022.txt")
    print(Fore.RED + Style.BRIGHT + "Welcome to the Dealership!")

    print("Please fill in the customer information below.\n")
    name = input(Fore.LIGHTBLUE_EX + "What is your name? :: " + Fore.WHITE)
    age = input(Fore.LIGHTBLUE_EX + "What is your age? :: " + Fore.WHITE)
    income = input(Fore.LIGHTBLUE_EX + "What is your annual income? :: " + Fore.WHITE)
    score = input(Fore.LIGHTBLUE_EX + "Enter your credit score (300-850) :: " + Fore.WHITE)
    record = input(Fore.LIGHTBLUE_EX + "Have you been in any car accidents before? (y/n) :: " + Fore.WHITE)

    customer = Customer(name, age, income, score, record)
    
    print(Fore.RESET + "\nThank you for entering your information! It will be used to help calculate the price of your purchase and any loan terms!")
    user_input = input(Fore.MAGENTA + "\nWould you like to view a visual breakdown of the dealership (y/n)? :: ")
    if (user_input == "y"):
        dealership.display_charts()
    running = True
    while(running):
        print(Fore.GREEN + "\nA car will now be purchased. Here are all the cars offered.\n")
        filtered_list = questionnaire(dealership.showroom)
        
        dealership.display(filtered_list)
        
        car_name = input(Fore.LIGHTYELLOW_EX + "\nEnter the make of the desired car :: " + Fore.WHITE)
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
    print("For full information about purchase, please review your receipt.")
    dealership.print_receipt(customer)
    
console_displayer()

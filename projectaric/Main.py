from Dealership import Dealership
from Customer import Customer
import colorama
from colorama import Fore, Style

def console_displayer():
    colorama.init(autoreset=True)
    dealership = Dealership(0.8, "car_shipment2022.txt")
    
    print(Fore.RED + Style.BRIGHT + "Welcome to the Dealership!")

    print("Please fill in the customer information below.\n")
    name = input(Fore.LIGHTBLUE_EX + "What is your name? :: " + Fore.WHITE)
    record = input(Fore.LIGHTBLUE_EX + "Have you been in any car accidents before? (y/n) :: " + Fore.WHITE)
    score = input(Fore.LIGHTBLUE_EX + "Enter your credit score (300-850) :: " + Fore.WHITE)
    in_col = input(Fore.LIGHTBLUE_EX + "Are you a college student? (y/n) :: " + Fore.WHITE)
    customer = Customer(name, score, in_col, record)#will use later when calculating msrp
    
    print(Fore.RESET + "\nThank you for entering your information! It will be used to help calculate the price of your purchase!")
    user_input = input(Fore.MAGENTA + "\nWould you like to view a visual breakdown of the dealership (y/n)? :: ")
    if (user_input == "y"):
        dealership.display_charts()
    running = True
    while(running):
        print(Fore.GREEN + "\nA car will now be purchased. Here are all the cars offered.\n")
        dealership.display_showroom()
        
        car_name = input(Fore.LIGHTYELLOW_EX + "\nEnter the make of the desired car :: " + Fore.WHITE)
        customer.owned_cars.append(dealership.sell(car_name))
        user_input = input(Fore.LIGHTMAGENTA_EX + "\nWould you like to buy another vehicle? (y/n) :: " + Fore.WHITE)
        if(user_input == "y"):
            pass
        else:
            running=False
    
    print(Fore.RESET + Fore.RED + "\nYou bought:")
    for car in customer.owned_cars:
        print(f"x1 {car.car_name}")
    print(f"The total payment due is ")
    print("For full information about purchase, please review your receipt.")
    
console_displayer()
#import classes
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#start the main code
make=CoffeeMaker()
menu=Menu()
is_on=True
money_machine=MoneyMachine()
while is_on:
    user_input=input(f"What would you like? ({menu.get_items()}): ")
    if user_input=='off':
        is_on=False
    elif user_input=='report':
        make.report()
    else:
        drink=menu.find_drink(user_input)
        
        if make.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            make.make_coffee(drink)


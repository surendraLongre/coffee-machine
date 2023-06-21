#import classes
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#start the main code
while True:
    user_input=input("What would you like? (espresso/latte/cappuccino): ")
    if user_input=='report':
    CoffeeMaker.report()

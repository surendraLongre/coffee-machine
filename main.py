MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#set initial moeny
money=0

#create function which will deduct user money and also check resources
def make_coffee(data):
    global money
    request=MENU[data]
    user_money=0
    #print(request)
    #get the money from the user
    print("Please enter coins.")
    user_money+=float(input("How many quarters?: "))*0.25
    user_money+=float(input("How many dimes?: "))*0.10
    user_money+=float(input("How many nickles?: "))*0.05
    user_money+=float(input("How many pennies?: "))*0.01
    user_money=round(user_money,2)

    #write code to check if the recourses are available

    #check money with the required money
    if user_money<request['cost']:
        print( "You entered less money, your drink is cannot be prepared")
    else:
        #reduce the resources which aer being used
        resources['water']-=request['ingredients']['water']
        resources['milk']-=request['ingredients']['milk']
        resources['coffee']-=request['ingredients']['coffee']
        money+=round(float(request['cost']), 2)
        print(f"Here is ${user_money-request['cost']} in change.")
        print(f"Here is your {data}. Enjoy!")




#start the main code
while True:
    user_request=input("What would you like? (espresso/latte/cappuccino): ")
    if user_request=='report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${money}")
    elif user_request!='espresso' and user_request!='latte' and user_request!='cappuccino':
        print("Wrong input")
    #write code to check if the recourses are available
    elif resources['water']<MENU[user_request]['ingredients']['water'] or resources['milk']<MENU[user_request]['ingredients']['milk'] or resources['coffee']<MENU[user_request]['ingredients']['coffee']:
        print("Not enough resources. Please check back later")
    else:
        make_coffee(user_request)


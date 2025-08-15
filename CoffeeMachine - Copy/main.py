MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

#This function generates a report that demonstrates the current resource values
def print_report(the_water, the_milk, the_coffee, the_money):
    print("Report:")
    print(f"Water: {the_water}ml\nMilk: {the_milk}ml\nCoffee: {the_coffee}g\nMoney: ${the_money}")

#This function calculates the amount of water and coffee it needs for an espresso
def espresso_option():
    the_espresso_water_usage = MENU["espresso"]["ingredients"]["water"]
    the_espresso_milk_usage = 0
    the_espresso_coffee_usage = MENU["espresso"]["ingredients"]["coffee"]

    return the_espresso_water_usage, the_espresso_milk_usage, the_espresso_coffee_usage

#This function calculates the amount of water, milk, and coffee it needs for latte and capuccino
def latte_or_cappuccino_option(the_user_coffee_option):
    latte_or_cappuccino_water_usage = MENU[the_user_coffee_option]["ingredients"]["water"]
    latte_or_cappuccino_milk_usage = MENU[the_user_coffee_option]["ingredients"]["milk"]
    latte_or_cappuccino_coffee_usage = MENU[the_user_coffee_option]["ingredients"]["coffee"]

    return latte_or_cappuccino_water_usage, latte_or_cappuccino_milk_usage, latte_or_cappuccino_coffee_usage

#This function will use the available resources in the machine depending on the coffee option selected
def use_resources(total_water, total_milk, total_coffee, coffee_water, coffee_milk, coffee_coffee):
    total_water -= coffee_water
    total_milk -= coffee_milk
    total_coffee -= coffee_coffee

    return total_water, total_milk, total_coffee

# This function will check if there are enough resources to make the coffee based on the user's selected coffee
# It will return a True or False
def check_resources(total_water_amount, total_milk_amount, total_coffee_amount, user_coffee_option):
    if user_coffee_option == "espresso":
        coffee_water_usage_ml, coffee_milk_usage_ml, coffee_usage_grams = espresso_option()

        if total_water_amount - coffee_water_usage_ml > 0 or total_coffee_amount - coffee_usage_grams > 0:
            return True
        else:
            return False
    else:
        coffee_water_usage_ml, coffee_milk_usage_ml, coffee_usage_grams = latte_or_cappuccino_option(user_coffee_option)

        if total_water_amount - coffee_water_usage_ml > 0 or total_milk_amount - coffee_milk_usage_ml > 0 or total_coffee_amount - coffee_usage_grams > 0:
            print(f"There's enough to make an {user_coffee_option}!")
            return True
        else:
            return False

#This function will let the user know what resource is the coffee machine low on
def running_low_resources(total_water_amount, total_milk_amount, total_coffee_amount):
    low_resource = ""

    if total_water_amount < 0 and total_milk_amount < 0 and total_coffee_amount < 0:
        low_resource = "water, milk, and coffee"
        return low_resource
    elif total_water_amount < 0 and total_milk_amount < 0:
        low_resource = "water, and milk"
        return low_resource
    elif total_water_amount < 0 and total_coffee_amount < 0:
        low_resource = "water, and coffee"
        return low_resource
    elif total_milk_amount < 0 and total_coffee_amount < 0:
        low_resource = "milk, and coffee"
        return low_resource
    elif total_water_amount < 0:
        low_resource = "water"
    elif total_milk_amount < 0:
        low_resource = "milk"
    elif total_coffee_amount < 0:
        low_resource = "coffee"

    return low_resource

#This function will ask the user for quarters, dimes, nickles and pennies to pay for their coffee
def insert_coins(the_coffee_option):
    total_cost = MENU[the_coffee_option]["cost"]
    total_sum = 0

    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickles = input("How many nickles?: ")
    pennies = input("How many pennies?: ")

    total_sum = float(quarters) * 0.25 + float(dimes) * 0.1 + float(nickles) * 0.05 + float(pennies) * 0.01

    if total_sum > total_cost:
        user_change = total_sum - total_cost
        print(f"Here is ${user_change} in change.")
        print(f"Here is your {the_coffee_option}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")



######################################################################################################################################################################

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
user_money = 0
total_charge = 0

#While loop starts here
coffee_option = input("What would you like? (espresso/latte/cappuccino):").lower()
are_there_enough_resources = check_resources(total_water_amount=water, total_milk_amount=milk, total_coffee_amount=coffee, user_coffee_option=coffee_option)

while are_there_enough_resources:
    if coffee_option == "espresso":
        espresso_water_usage, espresso_milk_usage, espresso_coffee_usage = espresso_option()
        new_espresso_amount_water, new_espresso_amount_milk, new_espresso_amount_coffee = use_resources(
            total_water=water, total_milk=milk, total_coffee=coffee, coffee_water=espresso_water_usage, coffee_milk=espresso_milk_usage, coffee_coffee=espresso_coffee_usage)

        water = new_espresso_amount_water
        milk = new_espresso_amount_milk
        coffee = new_espresso_amount_coffee

        insert_coins(the_coffee_option=coffee_option)

        coffee_option = input("What would you like? (espresso/latte/cappuccino):").lower()
        are_there_enough_resources = check_resources(total_water_amount=water, total_milk_amount=milk,
                                                     total_coffee_amount=coffee, user_coffee_option=coffee_option)
    else:
        coffee_water_usage, coffee_milk_usage, coffee_coffee_usage = latte_or_cappuccino_option(the_user_coffee_option=coffee_option)
        new_espresso_amount_water, new_espresso_amount_milk, new_espresso_amount_coffee = use_resources(
            total_water=water, total_milk=milk, total_coffee=coffee, coffee_water=coffee_water_usage, coffee_milk=coffee_milk_usage, coffee_coffee=coffee_coffee_usage)

        water = new_espresso_amount_water
        milk = new_espresso_amount_milk
        coffee = new_espresso_amount_coffee

        insert_coins(the_coffee_option=coffee_option)

        coffee_option = input("What would you like? (espresso/latte/cappuccino):").lower()
        are_there_enough_resources = check_resources(total_water_amount=water, total_milk_amount=milk,
                                                     total_coffee_amount=coffee, user_coffee_option=coffee_option)


while not are_there_enough_resources:
    the_low_resources = running_low_resources(total_water_amount=water, total_milk_amount=milk,
                                              total_coffee_amount=coffee)
    print(f"Sorry there is not enough {the_low_resources}.")

    coffee_option = input("What would you like? (espresso/latte/cappuccino):").lower()

    if coffee_option == "off":
        break

    are_there_enough_resources = check_resources(total_water_amount=water, total_milk_amount=milk,
                                                 total_coffee_amount=coffee, user_coffee_option=coffee_option)
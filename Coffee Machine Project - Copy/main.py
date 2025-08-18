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


def report(total_profit):
    """This function generates a report that demonstrates the current resource values"""
    for value in resources:
        print(f"{value}: {resources[value]}")

    print(f"Money: ${total_profit}")


def check_resources(water_container_ml, milk_container_ml, coffee_container_grams, the_coffee):
    """This function returns True or False if there is enough resources to make the coffee selected"""
    water_usage = MENU[the_coffee]["ingredients"]["water"]
    if the_coffee == "espresso":
        milk_usage = 0
    else:
        milk_usage = MENU[the_coffee]["ingredients"]["milk"]

    coffee_usage = MENU[the_coffee]["ingredients"]["coffee"]

    if water_container_ml - water_usage < 0 or milk_container_ml - milk_usage < 0 or coffee_container_grams - coffee_usage < 0:
        low_resource(water_container_ml, milk_container_ml, coffee_container_grams, the_coffee)
        return False
    elif water_container_ml > 0 and milk_container_ml > 0 and coffee_container_grams > 0:
        return True
    else:
        return False


def low_resource(water_container_ml, milk_container_ml, coffee_container_grams, the_coffee):
    """This function finds the resource(s) that are running low and someone needs to refill the containers"""

    water_usage = MENU[the_coffee]["ingredients"]["water"]

    if the_coffee == "espresso":
        milk_usage = 0
    else:
        milk_usage = MENU[the_coffee]["ingredients"]["milk"]

    coffee_usage = MENU[the_coffee]["ingredients"]["coffee"]

    if water_container_ml - water_usage < 0 and milk_container_ml - milk_usage < 0 and coffee_container_grams - coffee_usage < 0:
        return "water, milk, and coffee"
    elif water_container_ml - water_usage < 0 and milk_container_ml - milk_usage < 0:
        return "water, and milk"
    elif water_container_ml - water_usage < 0 and coffee_container_grams - coffee_usage < 0:
        return "water, and coffee"
    elif milk_container_ml - milk_usage < 0 and coffee_container_grams - coffee_usage < 0:
        return "milk, and coffee"
    elif water_container_ml - water_usage < 0:
        return "water"
    elif milk_container_ml - milk_usage < 0:
        return "milk"
    elif coffee_container_grams - coffee_usage < 0:
        return "coffee"

    return 0

def process_coins(total_profit, the_coffee):
    """This function will process the coins inserted, give change when necessary, and let the user know if there is not enough money to pay for the coffee."""
    total_sum = 0
    total_change = 0

    while MENU[the_coffee]["cost"] >= total_sum:
        print("Please insert coins.")
        quarters = int(input("How many quarters?")) * 0.25
        dimes = int(input("How many dimes?")) * 0.1
        nickles = int(input("How many nickles?")) * 0.05
        pennies = int(input("How many pennies?")) * 0.01

        total_sum = quarters + dimes + nickles + pennies
        total_cost = MENU[the_coffee]["cost"]
        total_change = total_sum - total_cost
        total_profit = total_cost

        if total_sum < total_cost:
            print("Sorry that's not enough money. Money refunded.")
            total_sum = 0

    return f"Here is ${total_change} in change.\nHere is your {the_coffee}. Enjoy!", total_profit


def make_coffee(water_container_ml, milk_container_ml, coffee_container_grams, the_coffee):
    """This function will take the current resources and deduct the current resources based on the coffee selected"""
    water_usage = MENU[the_coffee]["ingredients"]["water"]
    milk_usage = 0
    coffee_usage = MENU[the_coffee]["ingredients"]["coffee"]

    if the_coffee == "espresso":
        milk_usage = 0
    else:
        milk_usage = MENU[the_coffee]["ingredients"]["milk"]

    water_container_ml -= water_usage
    milk_container_ml -= milk_usage
    coffee_container_grams -= coffee_usage

    return water_container_ml, milk_container_ml, coffee_container_grams


profit = 0
is_on = True

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

while is_on:
    coffee_option = input("What would you like? (espresso/latte/cappuccino):")

    if coffee_option == "report":
        report(total_profit=profit)
    elif coffee_option == "off":
        break
    elif coffee_option in MENU:
        if check_resources(water_container_ml=water, milk_container_ml=milk, coffee_container_grams=coffee,
                           the_coffee=coffee_option):
            print("There's enough resources to make your coffee!")
            the_total_cost, the_total_profit = process_coins(total_profit=profit, the_coffee=coffee_option)

            print(the_total_cost)

            profit += the_total_profit

            new_water_amount, new_milk_amount, new_coffee_amount = make_coffee(water_container_ml=water,
                                                                               milk_container_ml=milk,
                                                                               coffee_container_grams=coffee,
                                                                               the_coffee=coffee_option)
            water = new_water_amount
            milk = new_milk_amount
            coffee = new_coffee_amount
            print(water)
            print(milk)
            print(coffee)

        else:
            the_low_resources = low_resource(water_container_ml=water, milk_container_ml=milk,
                                             coffee_container_grams=coffee, the_coffee=coffee_option)
            print(f"Sorry, there is not enough {the_low_resources}.")

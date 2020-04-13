# Breakfast Program
# Give the user the options for breakfast, take the order
# Get input and use it to determine what happens next
# Handle bad input without crashing
# Be flexible with the input the user can enter
# Print messages to the console, with a short pause after each one
# Allow the player to order again if they like

import time


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("Hello! I am Alfred, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause("Sorry, I don't understand.")


def get_order():
    response = valid_input('Please place your order. Would you like waffles or pancakes?\n',
                           ['waffles', 'pancakes'])
    if 'waffles' in response:
        print_pause("Waffles it is!")
    elif 'pancakes' in response:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly.")
    order_again()


def order_again():
    response = valid_input("Would you like to place another order? Please say 'yes' or 'no'?\n", ["yes",
                           "no"])
    if 'no' in response:
        print_pause("OK, goodbye!")
    elif 'yes' in response:
        print_pause("Very good, I'm happy to take another order.")
        get_order()


def order_breakfast():
    intro()
    get_order()


order_breakfast()
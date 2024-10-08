### RANDOM CHOICE AND INTEGER (ROLL FOR FREE PIZZA) ###

import random

pizza_list = ["margarita", "pepperoni", "chicken bbq", "pineapple"]

while True:
    print("Type 'roll' to get a random pizza of random quantity")

    try:
        user_input = input("> ")
    except KeyboardInterrupt:
        quit()

    try:
        if user_input == "roll":
            print(f"You got {random.randint(a=1, b=3)} {random.choice(pizza_list)} pizza(s)")
    except ValueError:
        print("Incorrect value")
### BASIC LIST (SHOPPING CART) ###

cart_list = []

loop = True

while loop:
    append_input = input("Enter a product: ")

    cart_list.append(append_input)
    print("Your cart: {}".format(cart_list))

    remove_input = input("Enter a product you want to remove (N = None): ")

    if remove_input.lower() == "n":
        pass
        # continue
    else:
        try:
            cart_list.remove(remove_input)
            print("Updated cart: {}".format(cart_list))
            # continue
        except ValueError:
            print("Unrecognised product!")
            # continue

    continue_input = input("Continue shopping? Y/N: ")

    if continue_input.lower() == "y":
        pass
        # continue
    elif continue_input.lower() == "n":
        print("Thanks for shopping with us!")
        loop = False
        # break
    else:
        print("Invalid choice!")
        # continue
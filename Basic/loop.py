### BASIC LOOP (REPEAT UNTIL AN ACCEPTED INPUT IS PROVIDED) ###

loop = True

while loop:
    user_input = input("Enter a password: ")

    if len(user_input) > 8:
        print("Password accepted!")
        loop = False
        # break
    else:
        print("Your password needs to be over 8 characters long!")
        # continue
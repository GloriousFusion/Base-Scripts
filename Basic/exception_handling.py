### BASIC EXCEPTION HANDLING (ADD 10 TO A NUMBER INPUT) ###

user_input = input("Enter a number: ")

try:
    print(float(user_input) + 10)
except ValueError:
    print("Only numbers (with decimals) accepted!")
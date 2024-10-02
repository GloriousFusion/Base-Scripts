### BASIC GLOBAL & LOCAL VARIABLES (EVEN OR ODD NUMBER CHECKER) ###

divider = 2 # Global variable

def odd_even(number): # Local variable
    if number % divider == 0:
        print("The number is Even")
    else:
        print("The number is Odd")

def user_input():
    input_number = int(input("Enter a number: "))
    odd_even(number=input_number)

user_input()
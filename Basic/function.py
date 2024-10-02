### BASIC FUNCTIONS (ADD & SUBTRACT CALCULATOR) ###

input_number_a = float(input("Enter number a: "))
input_number_b = float(input("Enter number b: "))

input_function = input("Enter function: ")

def addition():
    print(input_number_a + input_number_b)

def subtraction():
    print(input_number_a - input_number_b)

if input_function == "addition" or input_function == "+":
    addition()
elif input_function == "subtraction" or input_function == "-":
    subtraction()
else:
    print("Unrecognised input function")
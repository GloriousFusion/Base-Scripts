### BASIC CONDITIONS (GUESS THE NUMBER GAME) ###

number_a = 5
number_b = int(input("Enter a number: "))

if number_a > number_b:
    print("Your number is lesser than number a")
elif number_a < number_b:
    print("Your number is greater than number a")

# elif number_a == number_b:
#     print("Your number is the same as number a")

else: # Alternative way to check if the numbers are equal
  print("Your number is the same as number a")
### BASIC DICTIONARY & ITERATION (CAPITAL CITY FINDER) ###

country_capitals = {
    "England": "London",
    "Spain": "Madrid",
    "France" : "Paris",
    "Germany": "Berlin"
}

country_found = False # Check to see if one of the dictionary keys (countries) is found in the user's input

user_input = input("Enter a country: ")

for key, value in country_capitals.items():
    if user_input.capitalize() == key:
        print(f"The capital of {user_input} is {value}")
        country_found = True
        break # Stops the search once the key matches the input (works without it, but the iteration will keep on going)

if not country_found: # End of the iterative loop, as the loop itself checks for each key one by one.
    print("Sorry I could not find the capital of that country, try adding it into the dictionary?")
# variables for taco ingredients
tortilla = True
meat = "chicken"
cheese = True
guacamole = False
salsa = "mild"

print("Welcome to WindZoar's Taco Stand!")

# Can we make a taco?
if tortilla:
    print("Great! We can start our taco with a tortilla.")
else:
    print("Oh no! We dont have any tortillas. We cant make a taco!")
# Meat options
if meat == "chicken":
    print("Adding some delectable chicken to your taco!")
elif meat == "beef":
    print("So you want beef? Sounds good!")
elif meat == "pork":
    print("You like pork, huh? Adding delicios pork to your taco.")
else:
    print("Looks like you're going with vegeterian then!")
# Cheesy conditions
if cheese:
    print("Time for some cheese!")
    if salsa == "spicy":
        print("Adding some extra cheese to balance out the spiciness from the salsa!")
    else:
        print("Adding a normal amount of cheese.")
else:
    print("No cheese on this taco")

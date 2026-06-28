# Author: Elias Sjostrom
# Date: 6/28/26

# Getting the customer's name
customer_name = input ("Please enter your name: ")

# prices
sandwich_price = 8
platter_price = 12

# meal choice and set prices
meal_choice = input("Do you want a sandwich meal or platter meal? (sandwich/platter): ")
if meal_choice. lower () == "sandwich":
    meal_price = sandwich_price
elif meal_choice.lower() == "platter":
    meal_price = platter_price
else:
    print("Invalid choice. Defaulting to sandwich meal.")
    meal_choice = "sandwich"
    meal_price = sandwich_price

# ask for number of meals
num_meals = int(input("How many meals do you want?"))
total_cost = meal_price * num_meals

# extra sauce?
extra_sauce = input("Do you want extra sauce? (yes/no):")
if extra_sauce.lower() == "yes":
    total_cost += 0.50 * num_meals

#order summary
original_total = meal_price * num_meals
sauce_added = extra_sauce.lower() == "yes"
print("InOrder Summary:")
print("Customer Name: " + customer_name)
print("Meal Type: " + meal_choice + " meal")
print("Number of Meals: " + str(num_meals))
print("Extra Sauce: " + ("Yes" if sauce_added else "No"))
print("Original Total: $" + "{:.2f}". format(original_total))
print("Final Total: $" + "{:.2f}". format(total_cost))

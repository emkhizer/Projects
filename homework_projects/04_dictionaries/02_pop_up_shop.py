# Dictionary of fruits and their prices
fruits = {
    "apple": 1.5,
    "durian": 10.0,
    "jackfruit": 5.0,
    "kiwi": 2.0,
    "rambutan": 3.0,
    "mango": 4.0,
}

# Initialize total cost
total_cost = 0.0

# Loop through each fruit in the dictionary
for fruit, price in fruits.items():
    # Prompt the user for the quantity of the current fruit
    quantity = int(input(f"How many ({fruit}) do you want? "))
    # Calculate the cost for the current fruit and add it to the total cost
    total_cost += quantity * price

# Print the total cost
print(f"Your total is ${total_cost:.2f}")

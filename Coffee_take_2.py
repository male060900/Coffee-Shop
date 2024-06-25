# Make a menu
menu_main = {
    'Coffee': 2.5,
    'Hot Chocolate': 1.25,
    'Tea': 1.5
}

menu_side = {
    'Cake': 3.5,
    'Sweet Bread': 1.5,
    'Ice-Cream': 2.5
}
#this function prints the menu
def menu():
    print("Main Menu:")
    for item, price in menu_main.items():
        print(f"{item}: {price}")

    print("\nSide Menu:")
    for item, price in menu_side.items():
        print(f"{item}: {price}")

# Greet the customer
print("Welcome In\nHere is the Menu")
menu()

# Take their order
name = input("What is your name?\n")
# Need to loop back to ask to type main again!!!!!!
main = input("What Coffee would you like?\n")

# Validate main course selection 

if main not in menu_main:
    print("Invalid main course order.")
else:
    main_price = menu_main[main]

    sides_question = input("Would you like sides? Y/N\n")
    if sides_question.upper() == "Y":
        side_orders = []
        for i in range(2):  # Allow up to 2 sides
            side_order = input(f"Side {i+1} (or None for done):\n")
            if side_order.lower() == "none":
                break
            elif side_order not in menu_side:
                print("Invalid side order.")
            else:
                side_orders.append(side_order)
    
    # Calculate prices based on the side orders
    side_prices = sum(menu_side[order] for order in side_orders if order in menu_side)
    total_price = main_price + side_prices

    # Print receipt
    receipt = f"Name: {name}\nMain:\n{main}\nSides:\n{' '.join(side_orders)}"
    print("\nHere's your receipt:")
    print(receipt)

    # Print total price
    print(f"\nTotal: {total_price}")

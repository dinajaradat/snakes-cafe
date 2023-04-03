print("                                      ")
print("      Welcome to the Snakes Cafe!     ")
print("      Please see our menu below.      ")
print("                                      ")
print("   To quit at any time, type 'quit'   ")
print("                                      ")

menu = {
    "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "Desserts": ["Ice Cream", "Cake", "Pie"],
    "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
}

for section, items in menu.items():
    print(section)
    print("-" * len(section))
    for item in items:
        print(item)
    print()

print("                                   ")
print("   What would you like to order?   ")
print("                                   ")

orders = {}
while True:
    order = input("> ")
    if order == "quit":
        break
    elif order in menu["Appetizers"] + menu["Entrees"] + menu["Desserts"] + menu["Drinks"]:
        if order in orders:
            orders[order] += 1
        else:
            orders[order] = 1
        print(f"** {orders[order]} order(s) of {order} have been added to your meal **")
    else:
        print("Sorry, that item is not on the menu.")
print("Exiting")
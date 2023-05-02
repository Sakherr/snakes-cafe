

print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**                                  **")
print("** To quit at any time, type 'quit' **")
print("**************************************")

menu = {
    "Appetizers": ["wings", "cookies", "spring rolls"],
    "Entrees": ["salmon", "steak", "meat tornado", "a literal garden"],
    "Desserts": ["ice Cream", "cake", "pie"],
    "Drinks": ["coffee", "tea", "unicorn Tears"]
}

for section, items in menu.items():
    print("\n" + section + "\n" + "-" * len(section))
    for item in items:
        print(item)

print("\n" + "*" * 35)
print("** What would you like to order? **")
print("*" * 35)

orders = {}

while True:
    order = input("> ")
    if order.lower() == "quit":
        break
    found = False
    for section, items in menu.items():
        if order in items:
            found = True
            if order not in orders:
                orders[order] = 1
            else:
                orders[order] += 1
            print(f"** {orders[order]} order(s) of {order} have been added to your meal **")
            break
    if not found:
        print("Sorry, we don't have that item on our menu.")

for order, count in orders.items():
    print(f"{count} order(s) of {order}")

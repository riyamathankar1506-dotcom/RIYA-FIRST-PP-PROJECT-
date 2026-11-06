menu = {
    'Pizza': 149,
    'Cold coffee': 80,
    'Hot coffee': 30,
    'Momos': 60,
    'Burger': 59,
    'Fries': 49,
}

print("Welcome to TIMEPASS cafe")
print("Pizza: RS149\nCold coffee: RS80\nHot coffee: RS30\nMomos: RS60\nBurger: RS59\nFries: RS49")
order_total = 0

# 1. Takes first order, removes extra spaces, and auto-capitalizes the first letter
item_1 = input("What will you like to have = ").strip().capitalize()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not available yet!")

# 2. Handles yes/no input case-insensitively
another_order = input("any thing else?(yes/no) ").strip().lower()

if another_order == "yes":
    # 3. Takes second order with the same capitalization fix
    item_2 = input("Enter the name of second item = ").strip().capitalize()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"THE TOTAL AMOUNT OF ITEMS TO PAY IS RS {order_total}")

def add_item(cart, item_name, price, quantity):
    for i in range(len(cart)):
        if cart[i][0] == item_name:
            update_item(cart, item_name, price, quantity)
            return

    cart.append([item_name, price, quantity])
    print(f"{item_name} added with {quantity} units at ${price}.")

def remove_item(cart, item_name):
    for i in range(len(cart)):
        if cart[i][0] == item_name:
            cart.pop(i)
    print(f"{item_name} removed from the cart.")

def update_item(cart, item_name, price, quantity):
    for i in range(len(cart)):
        if cart[i][0] == item_name:
            cart[i][1] = price
            cart[i][2] = quantity
    print(f"{item_name} updated to {quantity} units at ${price}.")

def view_cart(cart):
    print("Items in your cart:")
    for item in cart:
        print(f"- {item[0]}: {item[2]} units at ${item[1]}")

def calc_total(cart):
    print(f"Total cost of items in cart: ${sum([item[1] * item[2] for item in cart]):.2f}")
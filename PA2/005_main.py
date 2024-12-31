import cart

def main():

    shopping_cart = []
    action = ""

    while action != "QUIT":
        action = input().upper()

        if action == "ADD":
            tmp = input().split()
            item_name = tmp[0]
            price = float(tmp[1])
            quantity = int(tmp[2])
            cart.add_item(shopping_cart, item_name, price, quantity)

        elif action == "REMOVE":
            item_name = input()
            cart.remove_item(shopping_cart, item_name)

        elif action == "UPDATE":
            tmp = input().split()
            item_name = tmp[0]
            price = float(tmp[1])
            quantity = int(tmp[2])
            cart.update_item(shopping_cart, item_name, price, quantity)

        elif action == "VIEW":
            cart.view_cart(shopping_cart)

        elif action == "TOTAL":
            cart.calc_total(shopping_cart)  

        elif action == "QUIT":
            print("Bye!")

if __name__ == "__main__":
    main()
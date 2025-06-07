from data import inventory, trans
import add_product
import buy_product

while True :
    action = int(input("ffkjj"))
    if action == 1 :
        name = input("шо там")
        add_product.add_product(name)
        print(inventory)

    elif action == 2 :
        name = input("шо там")
        buy_product.buy_product(name)
        print(inventory)
    elif action == 3 :
        pass
    elif action == 0 :
        break


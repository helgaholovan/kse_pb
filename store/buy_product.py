from data import inventory, trans
def buy_product(name) :
    if name in inventory :
        quantity = int(input("хав мач"))
        inventory[name]["quantity"] += quantity
        total = (inventory[name]["price"])*quantity
        print(total)
    else:
        print("pypypy")
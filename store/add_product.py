from data import inventory
def add_product(name) :
    if name in inventory:
        quantity = int(input("хав мач"))
        inventory[name]["quantity"] += quantity
    else:
        price = input("ґроши")
        quantity = input("хав мач")
        voc ={}
        voc["price"] = price
        voc["quantity"] = quantity
        inventory[name] = voc
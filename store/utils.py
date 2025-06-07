def is_valid_price(value) :
    if value>0 :
        res = True
    else :
        res = False
    return res

def is_valid_quantity(value) :
    if value>0 :
        res = True
    else :
        res = False
    return res

def format_currency(amount) :
    sss = "%.2f" %amount 
    return sss + " грн"


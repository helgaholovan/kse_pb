import random
import string
def generate_password(length, allow_symbols) :
    symb = string.ascii_lowercase
    SYmb = string.ascii_uppercase
    num = string.digits
    punct = string.punctuation
    if allow_symbols == False :
        SS = SYmb + symb + num
        ress = "".join(random.choices(SS, k=length))
    elif allow_symbols == True :
        SSS =SYmb + symb + num + punct
        ress = "".join(random.choices(SSS, k=length))

    return ress

print(generate_password(12, False))    
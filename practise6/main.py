import geometry
print(geometry.rectangle_area(4,6))
import converter
print(converter.usd_to_uah(1000,39.5))
import taxes
print(taxes.calculate_vat(15000)+taxes.calculate_income_tax(15000))
import math
print(math.sqrt(121))
print(math.sin(math.pi/2))
print(math.floor(7.8))
print(math.ceil(7.8))
import random
num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
print(num1)
print(num2)
print(f"Сума {num2+num1}")
import datetime
user_birthday = input("рррр-мм-дд")
birthday_date=datetime.datetime.strptime(user_birthday,"%Y-%m-%d")
today = datetime.date.today()
days_liv = (today-birthday_date.date()).days
print(days_liv)


bal = 10000
rand = random.random()
while bal>=100:
    if rand >= 1/37:
        bal = bal-100
        print(bal)
        continue
    else:
        print("Виграв")
        
    
    


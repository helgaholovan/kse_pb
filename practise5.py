#Task1
def calculate_vat(price) :
  pdv = 0.2
  result = price * pdv
  return result
calculate_vat(300)

#Task2
def usd_to_uah(amount) :
  curs = 39.5
  res = curs * amount
  return res

usd_to_uah(500)

#Task3
def monthly_salary(hours,rate) :
  res2 = hours*rate
  return res2
monthly_salary(3,33)

#Task4
def apply_discount(price, discount) :
  res3 = price* (100-discount)/100
  return res3
apply_discount(44, 40)

#Task5
def profit(revenue, cost, tax):
  res4 = (revenue - cost)*(1-tax)
  return res4
profit(1000, 100, 0.2)


#Task6
def weighted_average_price(prices, quantities) :
  total = 0
  for index,num in enumerate(prices) :
    total += prices[index]*quantities[index]
  dooo = sum(quantities)
  return total/dooo
weighted_average_price([2, 4, 5], [10, 5, 2])

#Task7
def calculate_wacc(equity, debt, cost_of_equity, cost_of_debt, tax_rate) :
  wacc = (equity/(equity+debt))*cost_of_equity + (debt/(equity+debt))*cost_of_debt*(1-tax_rate)
  return wacc
calculate_wacc(7, 7, 7, 7, 7)

#Task8
def monthly_payment(present_value, rate, months) :
 res8 = (present_value*rate)/(1-(1+rate)**(-months))
 return res8

monthly_payment(7, 7, 7)



#Task9
def analyze_prices(prices):
  voc = {}
  m = min(prices)
  ma = max(prices)
  av = sum(prices)/len(prices)
  count = 0
  for i in prices :
    if i<av :
      count = count + 1
  voc["мінімальне значення"] = m
  voc["максимальне значення"] = ma
  voc["середнє значення"] = av
  voc["кількість товарів дешевших за середнє"] = count
  return voc

analyze_prices([2,8,3])


#Бонусне
def adjust_for_inflation(income, inflation_rates) :
  liist = []
  for rate in inflation_rates :
    sss = income*rate
    ss = income+sss
    liist.append(ss)
  return liist
adjust_for_inflation(10000, [0.08, 0.1, 0.07])
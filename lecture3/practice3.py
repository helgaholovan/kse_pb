#Завдання1
number = int(input("Парне"))
if number%2==0 :
  print("sdfhsjhbd")
else:
  print("");

#Завдання2
number = float(input("середній бал"))
if number>=90 :
  print("Відмінник")
elif 89>=number>75:
  print("Молодець")
else :
  print("Старайся краще")

  #Завдання3
n = 10
while n<=100 :
  count = n*1.2
  print(f"Ціна без ПДВ: {n} грн  з ПДВ: {count} грн")
  n = n+5

  x = int(input("перше"))
y = int(input("друге"))
z = int(input("третє"))
if x>y and x>z :
  print(x)
elif y>x and y>z :
  print(y)
elif z>x and z>y :
  print(z)
else :
  print("sdfjbsk")

  m=0
n = 1000
while n<5000:
  n = n+300
  m = m+1
  print(f"Місяць - {m} , накопичено - {n}")

  year = int(input("Парне"))
if year%4 ==0 and year%100 or year%400 ==0 :
  print("Високосний")
else :
  print("Звичайний рік")

  x = 0
while x<20 :
  x = x+1
  if x%4==0:
    continue
  print(x)

  credit = 10000
month = 0
while credit>=0 :
  credit = (credit-1200)*1.02
  month = month + 1
  if credit > 0:
    print(f"{credit} за {month} місяць")



sum = 0
while True :
  income = float(input("sgbdjsgk"))
  if income == 0 :
    break
  elif income<0 :
    print("Дохід не може бути від'ємним")
    continue
  else :
    sum = sum + income
    print(f"Ваш дохід збережено:{sum}")
    

    
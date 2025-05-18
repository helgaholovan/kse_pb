#Завдання1
text = "Hello, Python World!"
print(text)

#Завдання2
x = int(input("Перше число"))
y = int(input("Друге число"))
suum = x+y
print(f"Сума {suum}")
vidn = x-y
print(f"Різниця {vidn}")
mnoj = x*y
print(f"Добуток {mnoj}")
dilen = x/y
print(f"Частка {dilen}")

#Завдання3
x = input("Напишіть щось")
y = input("Напишіть ще щось")
print(x + y)
print(f"Довжина рядку:{len(x + y)}")

#Завдання4
x = int(input("число"))
if x%2==0 :
    print("Парне")
else :
    print("Непарне")

 #Завдання5
for i in range(1,11) :
    print(i)

#Завдання6
num = int(input("num"))
if num>0 :
    print("Позитивний")
elif num<0 :
    print("Негативний")
else :
    print("Нуль")

#Завдання7
for i in range(1,11) :
    if i%2==0 :
        print(i)

#Завдання8
x = int(input("число"))
ssss = 0
for i in range(1,x+1) :
    ssss += i
print(ssss)

#Завдання9
for i in range(10,0,-1) :
    print(i)cd

#Завдання10
for i in range(1,11) :
    if i==5 :
        continue
    elif i==7 :
        break
    print(i)
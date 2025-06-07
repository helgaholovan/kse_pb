#Початковий рівень (5 завдань):
#1. Сума чисел: обчисліть суму чисел у списку.
lll = [2, 3, 4, 5]
print(sum(lll))
#2. Знайти мінімум: Визначити найменше число в списку.
print(min(lll))
#3. Перевертання списку: перевертання елементів у списку
print(lll[::-1])
#4. Друкувати непарні числа: відобразити всі непарні числа зі списку.
nl = []
for i in lll:
  if i%2 != 0 :
      nl.append(i)
print(nl)
#5. Помножити список: помножити кожен елемент у списку на задане число
oo = []
for i in lll:
  o = i*4
  oo.append(o)
print(oo)



#Легкий рівень (10 завдань):
#1. Фільтрувати за умовою: витягувати зі списку числа, більші за X
llln = [-1, 2, 3, 4, 5, 6, 12]
x = 3.5
blll = []
for i in llln:
  if i > x :
    blll.append(i)
print(blll)
#2. Середнє додатних чисел: Знайдіть середнє додатних чисел.
dd = []
for i in llln:
  if i > 0 :
    dd.append(i)
print(sum(dd))
#3. Максимум у відфільтрованому списку: знайдіть максимальну кількість чисел, менших за X.
mlll = []
for i in llln:
  if i < x :
    mlll.append(i)
print(max(mlll))
#4. Агрегована умовна сума: сума чисел, які діляться на Y.
ylll = []
y = 3
for i in llln:
  if i%y == 0 :
    ylll.append(i)
print(sum(ylll))
#5. Список квадратів: створіть список квадратів кожного числа.
klll = []
for i in llln:
  k = i**2
  klll.append(k)
print(klll)
#6. Витяг додатних чисел: створіть новий список лише з додатними числами з заданого списку.
ddll = []
for i in llln:
  if i > 0 :
    ddll.append(i)
print(dd)
#7. Фільтрувати рядки за префіксом: знайти всі рядки в списку, які починаються з указаного префікса.
words = [
    "apple",
    "application",
    "banana",
    "appetite",
    "approve",
    "bat",
    "apply",
    "cat",
    "append",
    "ant"
]
pres = "app"
pre = []
for i in words:
  if i.startswith(pres) :
    pre.append(i)
print(pre)
#8. Сума перших N чисел: обчисліть суму перших N чисел у списку
n = 4
nlll = sum(llln[:n])
print(nlll)
#9. Знайти всі паліндроми: видобути всі паліндромні рядки зі списку
notsinger = [
    "ротор",
    "довод",
    "казак",
    "око",
    "топот",
    "рівень",
    "кіт",
    "непаліндром",
    "комок",
    "анна",
    "алла",
    "ніжин",
    "тут",
    ]
plll = []
for i in notsinger :
  if i == i[::-1] :
    plll.append(i)
print(plll)
#10. Перевірка подільності: зі списку чисел створіть новий список логічних значень, де кожен елемент вказує, чи ділиться відповідне число на даний дільник.
hlll = []
num = 4
for i in llln:
  if i%num == 0:
    hlll.append(True)
  else:
    hlll.append(False)
print(hlll)


#Середній рівень (10 завдань):
#1. Фільтрувати за кількома умовами: числа, які діляться на X, але не діляться на Y.
lllnn = [-1, 2, 3, 4, 5, 6, 12]
dll = []
x = 2
y = 3
for i in lllnn : 
  if i %x == 0 and i %y != 0 :
    dll.append(i)
print(dll)
#2. Зведення вкладених списків: зведення списку списків в єдиний список.
vel = [[1, 2], [3, 4], [5, 6]]
mal = []
for i in vel :
  for ii in i :
    mal.append(ii)
print(mal)
#3. Складна маніпуляція рядками: виділіть і введіть великі літери в окремих підрядках.
gihh = ["HjNjBKjfjg", "HjbNjBff", "OKNMOknmONjM"]
big = []
for i in gihh :
  for ii in i :
    if ii.isupper():
      big.append(ii)
print(big)
#4. Багаторівневе сортування: сортування за спаданням, потім за частотою.
shojtakbagato = [4, 1, 2, 4, 3, 2, 4, 1, 3, 3, 2, 5, 5, 5]
voc = {}
for i in shojtakbagato :
  if i in voc:
    voc[i] +=1
  else:
    voc[i] = 1
sortll = []
for number, count in voc.items():
  sortll.extend([number]*count)
sortlll = sorted(sortll, reverse=True)
print(sortlll)

#5. Об’єднати списки умовно: об’єднати два списки на основі умов.
lllna = [3, 6, 7, 11, 12, 13]
res = []
for i in lllnn:
  if i%2==0 :
    res.append(i)
for i in lllna:
  if i%2!=0 :
    res.append(i)
print(res)
#6. Агрегація словника: сума значень у словнику за ключем.
slovnuchok = [("чай", 24), ("торитик",123),("солодке",45),("солодке",2),("чай",41)]
sss = {}
for key, value in slovnuchok:
    if key in sss :
      sss[key] += value
    else:
      sss[key] = value
print(sss)  
#7. Умовна заміна елементів: заміна елементів на основі стану
newlist = []
for i in lllnn :
  if i%2==0 :
    newlist.append("жіхх")
  else:
    newlist.append(i)
print(newlist)
#8. Підрахувати довжину рядків: підрахувати кількість рядків довжиною більше X.
chos = ["oiwnfiwnefwlf", "wjivnovqcwknc", "wjvf", "jgneirenj", "fh"]
zmis = 0
xx = 4
for i in chos:
  if len(i)>xx:
    zmis +=1
print(zmis)
#9. Об’єднати чергування: об’єднувати рядки по черзі з двох списків
kalamut = list(zip(chos,lllnn))
garno = []
for i in kalamut :
  for ii in i :
    garno.append(ii)
print(garno)
#10. Помножити, якщо: помножити числа на Y, якщо вони більші за X.
nareshti = []
for i in lllnn:
  if i >x :
    iy = i*y
    nareshti.append(iy)
print(nareshti)
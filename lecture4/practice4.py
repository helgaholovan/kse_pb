task1
nums = [3, 7, 2, 9, 5]
total = 0
i = 0
for num in nums :
  total += num
  i += 1
Av = total/i
print(Av)


Task2

nums = [4, 7, 2, 4, 8, 9, 2, 10, 3, 8]
emp = []
mun = nums.sort(reverse=True)
uni = set(nums)
unii = list(uni)
unii.sort(reverse=True)
for i in unii :
  if i%2==0 :
    emp.append(i)
print(emp)




Task3
grades = [
    [90, 85, 88],
    [75, 80, 79],
    [95, 92, 96],
    [88, 85, 84]
]
av = []
for i in grades :
  x = sum(i)/len(i)
  av.append(x)
y = max(av)
for i in range(len(av)) :
  if y==av[i] :
   print(grades[i])
print(y)
print(i)



Task4
prices = {
    "apple": 12,
    "banana": 8,
    "milk": 25,
    "bread": 20
}
sssum = sum(prices.values())
print(sssum)




Task5
people = {
    "Anna": "Kyiv",
    "Bohdan": "Lviv",
    "Oksana": "Kyiv",
    "Dmytro": "Odesa"
}
city = people.values()

cityy = list(set(city))
name = people.keys()
namee = list(set(name))
new_dick ={}
for i in cityy :
  new_dick[i]=[]
for key,value in people.items() :
  new_dick[value].append(key)
print(new_dick)

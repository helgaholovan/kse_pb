name = "ccc"
age = 123
city = "AAA"
country = "BBB"
year = 1234
dog = False
cat = True
smart = "very"
rate = 5.4
kkk = None

a = 3
b = 5

c = a
a = b
b = c

print(a)
print(b)

x = 3
y = 9
print(2*x+3*9)
print(x**2+2*x*y+y**2)
print((2/8)*x-(13/7*y))
print(y**(4*x-2*y)**(1/2))
print(y % x)
print((y/x)**2)
print(x>y)
print(x**2!=y)

P = 9999999999999999999
N = "щось"
print(f"{N} дорівнює {P} гривень")

x1 = 1
x2 = 2
x3 = 3
x4 = 4
((x1>x3)or(x2>x4))and not(x2!=x3)or(x1==x4)


height = int(input("Ведіть свій зріст"))
weight = int(input("Ведіть свою вагу"))
bmi = weight/(height**2)
print(f"При вазі {weight} метрів і рості {height} Ваш ВМІ складає {bmi}")

S1 = 3.14*30**2
print(S1)
S2 = 3.14*36**2
print(S2)
diff = ((100*S2/S1)-100)
print(diff)
rrr = "%.2f" % diff
print(f"Друга піца на {rrr}% більша за першу")
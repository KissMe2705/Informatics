from math import sqrt

x = float(input("Введите x: "))
a = float(input("Введите a: "))
y = float(input("Введите y: "))
b = float(input("Введите b: "))

z = 2*(x**6)**(1/4)*(x + a)+y**b

print(f"z = {z}")
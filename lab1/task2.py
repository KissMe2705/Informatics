from math import cos, log, sin, exp, sqrt

x = float(input("Введите значение переменной x: "))
y = float(input("Введите значение переменной y: "))
z = float(input("Введите значение переменной z: "))

a = sqrt(z**3 / 2) - sin(y)
b = exp(2) / 3 - cos(y) + z + log(y)

print(f"Получено значение функции a = {a}")
print(f"Получено значение функции b = {b}")

import math # библиотечность

# вводим градусы
x = float(input())

# переводим в радианы
# r = x * math.pi / 180 - сначала сделал так, но прочитал примечание
r = math.radians(x)

# считаем по формуле
z = math.sin(r) + math.cos(r) + math.tan(r) ** 2

# готовченко
print(z)
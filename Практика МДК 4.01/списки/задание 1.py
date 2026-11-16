prices = [100, 50, 200, 150 ]

print("Самая дорогая цена:", max(prices))
print("Самая дешевая цена:", min(prices))

print("Средняя цена:", sum(prices)/ len(prices))

print(*prices, sep=",")

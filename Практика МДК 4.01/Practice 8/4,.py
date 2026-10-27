population = int(input("Введите изначальный количество организмов: "))
percent = int(input("Введите среднесуточный прирост в процентах: "))
days = int(input("Введите количество дней: "))

for day in range(1, days + 1):
    growth = population * percent / 100
    population = population + growth
    print(f"День {day}. Размер популяции — {int(population)}")

n = int(input())

total_sum = 0 

# Сам Цикл
for i in range(1, n + 1):
    
    if i % 2 != 0:
        # просто прибавляем это число к сумме
        total_sum += i
    else:
        # если шаг четный (остаток равен 0), то ВЫЧИТАЕМ
        total_sum -= i

print(total_sum)
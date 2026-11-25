numbers = list(map(int,input("Введите числа:").split()))
pairs = 0
for i in range (len(numbers)):
    for j in range ( i+ 1, len(numbers)):
        if numbers [i] == numbers [j]:
            pairs += 1
print(pairs)

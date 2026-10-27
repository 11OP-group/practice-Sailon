n = int(input("Введите количество чисел: "))

biggest = 0
biggest2 = 0

print("Введите сами числа:")

for i in range(n):
    number = int(input())
    if number > biggest:
        biggest2 = biggest
        biggest = number
    else:
        if number > biggest2:
            biggest2 = number

print(f"Наибольшее число: {biggest}")
print(f"Второе наибольшее: {biggest2}")
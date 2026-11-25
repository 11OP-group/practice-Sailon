ip = input("Введите числа:")
parts = ip.split(".")

correct = True
for part in parts:
    if not 0 <= int(part) <= 255:
        correct = False

if correct:
    print("Да")
else:
    print("нет")


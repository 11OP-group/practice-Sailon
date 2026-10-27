import random

number = random.randint(1, 10)
answer = False

print(f" Я загадал число от 1 до 10. У вас 3 попытки, чтобы отгадать его)")

for attempt in range(1, 3 + 1):
    print(f"\nПопытка номер {attempt}")
    guess = int(input(f"Введите число: "))
    if guess == number:
        print("Верно! Молодец!")
        answer = True
        break
    else:
        if guess < number:
            print("Неправильно, загаданное число больше")
        else:
            print("Неправильно, загаданное число меньше")

if not answer:
    print(f"К сожалению( Вы не угадали! Верное число было {number}")
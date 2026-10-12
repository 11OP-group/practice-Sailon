# стоимость напитков в меню
COFFEE = 120
TEA = 80
JUICE = 100
WATER = 50
LEMONADE = 90

# размер всех скидок
STUDENT = 20
SALE10 = 10

print("☕ Меню кафе:")
print(f"1. Кофе ☕ - {COFFEE} руб")
print(f"2. Чай 🍵 - {TEA} руб")
print(f"3. Сок 🧃 - {JUICE} руб")
print(f"4. Вода 💧 - {WATER} руб")
print(f"5. Лимонад 🍋 - {LEMONADE} руб")
print()

drink = input("Введите номер напитка (1-5) или его название: ").strip().lower()

# выбираем напитки
match drink:
    case "1":
        name = "Кофе"
        emoji = "☕"
        price = COFFEE
    case "2":
        name = "Чай"
        emoji = "🍵"
        price = TEA
    case "3":
        name = "Сок"
        emoji = "🧃"
        price = JUICE
    case "4":
        name = "Вода"
        emoji = "💧"
        price = WATER
    case "5":
        name = "Лимонад"
        emoji = "🍋"
        price = LEMONADE

# применение наших скидок
discount = 0
card = input("У вас есть студенческий билет, чтобы получить скидку? (да/нет): ").strip().lower()
if card == "да":
    discount = STUDENT
else:
    sale = input("У вас есть карта нашего заведения? (да/нет): ").strip().lower()
    if sale == "да":
        discount = SALE10

final_price = price - (price * discount / 100)

# вывод результата
print()
print("╔════════════════════════════════╗")
print("║           🧾  ЧЕК  🧾          ║")
print("╚════════════════════════════════╝")
print()
print("=" * 40)
print(f"  {emoji}  Вы выбрали: {name}")
print("=" * 40)
print(f"  💵 Цена без скидки:  {price} руб")
if discount > 0:
    print(f"  🏷️ Скидка:           {discount}%")
    print(f"  📥 К оплате:    {final_price:.0f} руб")
else:
    print(f"  📥 К оплате:    {final_price:.0f} руб")
print("=" * 40)

using System;

namespace GladiatorBattle
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Random rand = new Random();

            Console.WriteLine("=== GLADIATOR BATTLE ===\n");

            int health1, armor1, health2, armor2;

            // Ввод данных первого гладиатора
            Console.Write("Введите здоровье первого гладиатора: ");
            if (!int.TryParse(Console.ReadLine(), out health1) || health1 <= 0)
            {
                Console.WriteLine("Ошибка: здоровье должно быть положительным числом!");
                Console.ReadLine();
                return;
            }

            Console.Write("Введите броню первого гладиатора (%): ");
            if (!int.TryParse(Console.ReadLine(), out armor1) || armor1 < 0)
            {
                Console.WriteLine("Ошибка: броня должна быть числом от 0 и выше!");
                Console.ReadLine();
                return;
            }

            // Ввод данных второго гладиатора
            Console.Write("Введите здоровье второго гладиатора: ");
            if (!int.TryParse(Console.ReadLine(), out health2) || health2 <= 0)
            {
                Console.WriteLine("Ошибка: здоровье должно быть положительным числом!");
                Console.ReadLine();
                return;
            }

            Console.Write("Введите броню второго гладиатора (%): ");
            if (!int.TryParse(Console.ReadLine(), out armor2) || armor2 < 0)
            {
                Console.WriteLine("Ошибка: броня должна быть числом от 0 и выше!");
                Console.ReadLine();
                return;
            }

            // Ограничение брони 100%
            if (armor1 > 100) armor1 = 100;
            if (armor2 > 100) armor2 = 100;

            // Случайная сила удара (10-50)
            int attack1 = rand.Next(10, 51);
            int attack2 = rand.Next(10, 51);

            // Урон с учётом брони
            int damage1 = attack1 - (attack1 * armor1 / 100);
            int damage2 = attack2 - (attack2 * armor2 / 100);

            // Новое здоровье
            int newHealth1 = health1 - damage2;
            int newHealth2 = health2 - damage1;

            if (newHealth1 < 0) newHealth1 = 0;
            if (newHealth2 < 0) newHealth2 = 0;

            // Вывод результатов
            Console.WriteLine("\n=== РЕЗУЛЬТАТЫ БОЯ ===");
            Console.WriteLine($"Первый гладиатор: удар {attack1}, урон {damage1}, здоровье: {newHealth1}");
            Console.WriteLine($"Второй гладиатор: удар {attack2}, урон {damage2}, здоровье: {newHealth2}\n");

            // Ветвление — определение победителя
            if (newHealth1 == 0 && newHealth2 == 0)
            {
                Console.WriteLine("Оба гладиатора погибли. Ничья.");
            }
            else if (newHealth1 == 0)
            {
                Console.WriteLine("Победил второй гладиатор!");
            }
            else if (newHealth2 == 0)
            {
                Console.WriteLine("Победил первый гладиатор!");
            }
            else if (newHealth1 > newHealth2)
            {
                Console.WriteLine("Победил первый гладиатор! У него больше здоровья.");
            }
            else if (newHealth2 > newHealth1)
            {
                Console.WriteLine("Победил второй гладиатор! У него больше здоровья.");
            }
            else
            {
                Console.WriteLine("Ничья! У обоих одинаковое здоровье.");
            }

            Console.ReadLine();
        }
    }
}
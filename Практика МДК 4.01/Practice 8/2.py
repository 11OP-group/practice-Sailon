all_even = True

for i in range(10):
    num = int(input())
    if num % 2 != 0:  # Типа число нечётное
        all_even = False

if all_even:
    print("YES")
else:
    print("NO")
for i in range(3):
    password = input("Введите пароль:")
    
    if password == "admin":
        print("Доступ разрешен")
        break
    else:
        print("Вход разблокирован")
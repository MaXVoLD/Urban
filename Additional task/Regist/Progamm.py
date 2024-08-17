from Class import *
from Welcome import *

print(welcom)  # Приветствие


def auth():
    # Программа:
    data_base = Base()  # Создал БД в переменной
    while True:  # Запуск программы в бесконечный цикл
        user = Check()  # Создал переменную класса Check для проверки логина
        password = Check()  # Создал переменную класса Check для проверки надежности пароля
        user.check_login(input('Введие логин: '))  # Запросил данные у пользователя для проверки
        if user.login is None:
            continue
        else:
            password.check_password(input('Введите пароль: '), input('Повторите пароль: '))
            if password.password is None:
                continue
            else:
                data_base.add_user(user.login, password.password)  # Полученные данные отправляю в словарь
    print(data_base.data)


auth()

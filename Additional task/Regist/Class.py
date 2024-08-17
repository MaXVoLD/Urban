class Base:
    '''
    Класс для хранения и обновления базы данных.
    Логины проверяются на уникальность
    '''

    def __init__(self):
        self.data = {}  # Создали пустой словарик для хранения данных

    def add_user(self, login, password):  # Проверяем уникальность логина
        if login in self.data.keys():
            print(f'Пользователь с логином "{login}" уже существует!\nПридумайте новый логин')
        else:
            self.data[login] = password
            print(f'Пользователь с логином "{login}" успешно добавлен!')
            print(f'\nБаза данных:\n{self.data}')  # Вывод в консоль словаря для проверки
            self.confirmation()

    def confirmation(self):  # Подтверждение продолжения добавления / выхода из программы
        choice = input('\nДобавить еще одного пользователя?'
                       '\nВведите "д" или "н"'
                       '\n=> ')
        if choice == 'д':
            print('Добавление нового пользователя')
        elif choice == 'н':
            print('Программа завершена!')
            exit()
        else:
            print('Введено некорректное значние!')
            self.confirmation()


class Check:
    '''
    Класс для проверки данных пользователя:
    Соответветствие пароля заданным параметрам параметрам:
    1) Длинна пароля не менее 8 символов;
    2) Совпадают ли пароль и повторный ввод пароля
    '''

    def __init__(self):
        self.cPassword = None
        self.login = None
        self.password = None

    def check_password(self, password, cPassword):  # Проверка пароля на соответствие параметрам
        check = []  # Дополнительный список для проверки
        err = []  # Список найденных ошибок
        if 8 <= len(password) <= 30:  # Длинна пароля
            check.append(True)
        else:
            check.append(False)
            err.append('Пароль должен содержать от 8 до 30 символов.')
        if password == cPassword:  # Совпадение паролей
            check.append(True)
        else:
            check.append(False)
            err.append('Пароли не совпадают.')
        for i in password:  # Заглавня буква
            if i.isupper():
                check.append(True)
                break
            else:
                check.append(False)
                err.append('Пароль должен содержать одну заглавную букву.')
                break
        if False in check:  # Если есть ошибки - выводим в консоль
            print('При вводе пароля не соблюдены следующие условия:\n')
            for i in err:
                print(i)
        else:
            self.password = password

    def check_login(self, login):
        check = []  # Дополнительный список для проверки
        err = []  # Список найденных ошибок
        if 4 <= len(login) <= 20:  # Длинна логина
            check.append(True)
        else:
            check.append(False)
            err.append('Логин должен содержать от 4 до 20 символов.')
        if login[0].isupper():
            check.append(True)
        else:
            check.append(False)
            err.append('Логин должен начинаться с большой буквы.')
        if False in check:  # Если есть ошибки - выводим в консоль
            print('При вводе логина не соблюдены следующие условия:\n')
            for i in err:
                print(i)
        else:
            self.login = login

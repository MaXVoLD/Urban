def pass_word():
    list_value = []  # Список для хранения списков пар значений
    list_password = []  # Список для хранения значиний после объеденения списков внутри list_value
    n = int(input('Введите число от 3 до 20: '))
    if 3 > n > 20:
        print('''
Введено неверное значние,
повторите попытку.
        ''')
        pass_word()
    else:
        for i in range(1, n):
            for j in range(1, n):
                if all([n % (i + j) == 0,
                        i != j,
                        [j, i] not in list_value]):
                    list_value.append([i, j])  # подобрал уникальные значения пар

    for i in list_value:
        list_password.extend(i)  # распаковал внутренние списки и объеденил их в один список

    password = ''.join(str(x) for x in list_password)  # перебрал значения из списка, присвоил их переменой
    print(password)


pass_word()

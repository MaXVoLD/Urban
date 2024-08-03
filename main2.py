import random

random_number = random.randint(3, 20)


def pass_word():
    list_value = []  # Список для хранения списков пар значений
    list_password = []  # Список для распаковки list_value
    print(f'Случайное число: {random_number}')
    for i in range(1, random_number):
        for j in range(1, random_number):
            if all([random_number % (i + j) == 0,  # Сумма пар должна быть кратна random_number
                    i != j,  # Пара не должна состоять из одинаковых чисел
                    [j, i] not in list_value]):  # Пара не должна быть реверсивной [[3 , 1] , [1 , 3]]
                list_value.append([i, j])  # Добавляем уникальные пары в list_value

    for i in list_value:
        list_password.extend(i)  # Перебираем внутренние списки и объеденяем их в один

    password = ''.join(str(x) for x in list_password)  # Распаковываем список без запятых и пробелов
    print(password)


pass_word()

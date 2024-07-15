def value():
    n = int(input('Введите целое число: '))
    while n < 0:
        print('\nВведено отрицательное число!'
              '\nПовторите попытку ниже:'
              '\n')
        value()
    else:
        for i in range(n, 0, -1):
            print(i * '*')
value()
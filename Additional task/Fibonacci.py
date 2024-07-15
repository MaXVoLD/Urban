def fibonacci():
    n = int(input('Введите любое число от 1 до 100: '))
    if 0 > n >= 100:
        print(f'Число {n} Не соответствует условиям.'
              f'\nПовторите попытку ниже.\n')
        fibonacci()
    else:
        count = 0
        a, b = 0, 1
        while count <= n:
            print(b, end=' ')
            a, b = b, b + a
            count += 1
    print('\nКод завершён!')
fibonacci()
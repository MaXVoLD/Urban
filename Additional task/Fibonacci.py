def fibonacci():
    n = int(input('Введите необходимое количество чисел'
                  '\nв последовательности (от 1 до 100): '))
    if n < 1 or n > 100:
        print(f'Число {n} Не соответствует условиям.'
              f'\nПовторите попытку ниже.\n')
        fibonacci()
    else:
        a, b = 0, 1
        for i in range(n):
            print(b, end=' ')
            a, b = b, b + a


fibonacci()
print('\nКод успешно завершён!')

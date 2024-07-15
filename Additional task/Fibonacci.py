def fibonacci():
    n = int(input('Введите необходимое количество чисел'
                  '\nв последовательности (от 1 до 100): '))
    if n < 1 or n > 100:
        print(f'Число {n} Не соответствует условиям.'
              f'\nПовторите попытку ниже.\n')
        fibonacci()
    else:
        count = 0
        a, b = 0, 1
        while count <= n - 1:
            print(b, end=' ')
            a, b = b, b + a
            count += 1


fibonacci()
print('\nКод успешно завершён!')

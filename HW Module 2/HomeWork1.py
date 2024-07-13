first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    equal = 3
elif first == second or first == third or second == third:
    equal = 2
else: equal = 0
print(f'Количество одинаковых чисел: {equal}')
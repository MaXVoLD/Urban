example = 'Random'
print('Первый символ строки: ', example[0])
print('Последний символ строки: ', example[-1])
print('Вторая половина строки: ', example[3:])
print('Строка наоборот: ', example[::-1])
print('Каждый второй символ строки: ', example[1::2])
print('')
print('=====Через переменную input=====')

#Через переменную Input:
example = input(str('Введите значение из 5ти символов: '))
print('Первый символ строки: ', example[0])
print('Последний символ строки: ', example[-1])
print('Вторая половина строки: ', example[3:])
print('Строка наоборот: ', example[::-1])
print('Каждый второй символ строки: ', example[1::2])
#Работа со словарём

print('\tРабота со словарём:')
my_dict = {'Sveta': 1994, 'Masha': 1997, 'Anton': 1987, 'Max': 1990}
print('1. Первоначальный словарь: ' , my_dict)
print('2. Значение по существующему ключу "Sveta": ' , my_dict.get('Sveta'))
print('3. Значение по несуществующему ключу "Karina": ' , my_dict.get('Karina'))
print('4. То же самое, только в одну строчку: ' , my_dict.get('Sveta'), ';', my_dict.get('Karina'))
my_dict.update({'Natasha': 2005 , 'Marina': 1999}) #Добавление новых значений в словарь
del_ = my_dict.pop('Max') #Удаление одной пары из словаря
print('5. Значение удалённого ключа "Max: "' , del_)
print('6. Обновлённый словарь: ' , my_dict)


#Работа с множеством

print('\n\tРабота с множеством:')
my_set = {1, 2.0, 1, 2.0, 'Stage', (1, 2, 3)}
print('1. Первоначальное множество: ', my_set)
my_set.update([5, 'Six']) #Добавление двух новых элементов в множество
my_set.discard(2.0) #Удаление одного элемента из множества
print('2. Обновлённое множество: ' , my_set)
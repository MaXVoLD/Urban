def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(25, False, 'string')
print_params(b=25)
print_params(c=[1, 2, 3])
print('===')

values_list = ['string', [1, 2], 58]
values_dict = {'a': 50, 'b': 'Johan', 'c': 80.6}

print_params(*values_list)
print_params(**values_dict)
print('===')

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

immutable_var = 1, 2.0, 'Hello world!', [0, 1]
print(immutable_var)
# immutable_var [0] = 3 #Кортеж относится к неизменяемым объектам, однако, он может в себя включать изменяемые, например списки.
# print(immutable_var)
mutable_list = (["Juice", 'Vine', 'Beer'])
mutable_list [0:1] = ['Scotch']
print(mutable_list)
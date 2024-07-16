def get_matrix():
    n = int(input('Введите количество строк: '))
    m = int(input('Введите количество столбцов: '))
    value = int(input('Введите любое число: '))
    matrix = []
    for i in range(1, n + 1):
        list_ = []
        matrix.append(list_)
        for j in (1, m):
            list_.append(value)
    print(matrix)


get_matrix()

def get_matrix(n, m, value):
    matrix = []
    for i in range(1, n + 1):
        list_ = []
        matrix.append(list_)
        for j in range(1, m + 1):
            list_.append(value)
    print(matrix)


get_matrix(2, 4, 10)

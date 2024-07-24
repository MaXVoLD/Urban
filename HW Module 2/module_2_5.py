def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        list_ = []
        matrix.append(list_)
        for j in range(m):
            list_.append(value)
    print(matrix)


get_matrix(2, 2, 10)
get_matrix(3, 5, 42)
get_matrix(4, 2, 13)

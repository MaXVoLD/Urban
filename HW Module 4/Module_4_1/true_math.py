from math import inf  # Импорт бесконечнечности из библиотеки math


def divide(first, second):
    if second != 0:
        result = first / second
        return result
    else:
        return inf

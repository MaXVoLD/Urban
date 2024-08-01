def function_f(n):
    answer = 0
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        answer = function_f(n / 2)
        return answer
    elif n % 2 != 0:
        answer = 1 + function_f(n - 1)
        return answer


def count():
    summ = 0
    for i in range(900):
        function_f(i)
        if function_f(i) == 9:
            summ += 1
    return summ


print(count())

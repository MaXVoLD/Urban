def function_f(n):
    answer = 0
    if n <= 1:
        return 0
    elif n > 1 and n % 2 != 0:
        answer = function_f(n - 1) + 3 * n ** 2
        return int(answer)
    elif n > 1 and n % 2 == 0:
        answer = n / 2 + function_f(n - 1) + 2
        return int(answer)


result = function_f(49)
print(result)

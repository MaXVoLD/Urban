def function_f(n):
    answer = 0
    if n <= 2:
        return 1
    else:
        answer = function_f(n - 1) + 2 * function_f(n - 2)
        return answer


result = function_f(7)
print(result)

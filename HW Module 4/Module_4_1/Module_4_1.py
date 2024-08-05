from fake_math import divide as divide_fake  # Импорт Fake деления на ноль
from true_math import divide as divide_true  # Импорт True деления на ноль

result1 = divide_fake(69, 3)  # Вычисление по Fake
result2 = divide_fake(3, 0)  # Вычисление по Fake
result3 = divide_true(49, 7)  # Вычисление по True
result4 = divide_true(15, 0)  # Вычисление по True
# Вывод результатов вычисления в консоль:
print(result1)
print(result2)
print(result3)
print(result4)

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

SIZE = 20
MIN_COUNT = 0
MAX_COUNT = 50
array = [randint(MIN_COUNT, MAX_COUNT) for _ in range(SIZE)]
min_ = array[0]
max_ = array[0]
sum_number = 0
for a in array:
    if a < min_:
        min_ = a
    elif a > max_:
        max_ = a
    sum_number += a
print(array)
print(f'Min- {min_}, Max - {max_}')
print(f'Сумма цифр без min и max- {sum_number - max_ - min_}')

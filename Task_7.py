# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint

SIZE = 50
MIN_COUNT = -50
MAX_COUNT = 50
array = [randint(MIN_COUNT, MAX_COUNT) for _ in range(SIZE)]
min_1 = array[0]
min_2 = array[1]
for a in array:
    if a < min_1:
        min_2 = min_1
        min_1 = a
    elif a < min_2:
        min_2 = a
print(array)
print(min_1, min_2)

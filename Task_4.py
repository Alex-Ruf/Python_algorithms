# Определить, какое число в массиве встречается чаще всего.
from random import randint

SIZE = 1000
MIN_COUNT = 1
MAX_COUNT = 100
array = [randint(MIN_COUNT, MAX_COUNT) for _ in range(SIZE)]
print(array)
max_count = 0
max_number = []
for i in set(array):
    count = 0
    for a in array:
        if a == i:
            count += 1
    if count > max_count:
        max_count = count
        max_number = [i]
    elif count == max_count:
        max_number.append(i)
for q in max_number:
    print(f'{q}', end=" ")
print(f'- {max_count} раз', end="")

import random, sys
from collections import Counter

MIN_COUNT = 1
MAX_COUNT = 1000


def result_1(n):
    array = [random.randint(MIN_COUNT, MAX_COUNT) for _ in range(n)]
    array_set = set(array)
    max_count = 0
    max_number = []
    for i in array_set:
        count = 0
        for a in array:
            if a == i:
                count += 1
        if count > max_count:
            max_count = count
            max_number = [i]
        elif count == max_count:
            max_number.append(i)

    return vars()


def result_2(n):
    array = [random.randint(MIN_COUNT, MAX_COUNT) for _ in range(n)]
    array_set = set(array)
    max_count = 0
    max_number = []
    for i in array_set:
        a = array.count(i)
        if a > max_count:
            max_count = a
            max_number = [i]
        elif a == max_count:
            max_number.append(i)
    return vars()


def result_3(n):
    array = [random.randint(MIN_COUNT, MAX_COUNT) for _ in range(n)]
    counter = Counter(array)
    max_count = 0
    max_number = []
    for i in dict(counter):
        if dict(counter)[i] == max(counter.values()):
            max_number.append(i)
            max_count = max(counter.values())
    return vars()


def getsizeof(n):
    sum_ = []
    sum_.append(sys.getsizeof(n))

    if hasattr(n, '__iter__'):
        if hasattr(n, 'items'):
            for key, value in n.items():
                sum_.append(sys.getsizeof(value))
                sum_.append(sys.getsizeof(key))
                if not isinstance(value, int):
                    for i in value:
                        sum_.append(sys.getsizeof(i))

        elif not isinstance(n, str):
            for item in n:
                sum_.append(sys.getsizeof(item))
                getsizeof(item)

    return f'Сумма выделенной памяти всех переменных- {sum(sum_)} байт'


print(getsizeof(result_1(1000)))    # Сумма выделенной памяти всех переменных- 88721 байт
print(getsizeof(result_2(1000)))    # Сумма выделенной памяти всех переменных- 88415 байт
print(getsizeof(result_3(1000)))    # Сумма выделенной памяти всех переменных- 73855 байт
print(getsizeof(result_1(100000)))    # Сумма выделенной памяти всех переменных- 3686465 байт
print(getsizeof(result_2(100000)))    # Сумма выделенной памяти всех переменных- 3686383 байт
print(getsizeof(result_3(100000)))    # Сумма выделенной памяти всех переменных- 3690347 байт


# 1-2 вариант используют списки и множества, 3 вариант использует коллекцию.
#  1- 2 вариант тратят  на много больше  времени на расчет , чеи 3 вариант , а памяти занимаю одинаково.
# Поэтому 3 вариант наилучший  по времени и занимаемой памяти.
# ОС Ubuntu 20.04 x64 и Python 3.8
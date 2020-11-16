
import timeit,cProfile
import random
from collections import Counter

MIN_COUNT = 1
MAX_COUNT = 1000

def result_1(n):

    array = [random.randint(MIN_COUNT, MAX_COUNT) for _ in range(n)]
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

    return max_count, max_number


def result_2(n):

    array = [random.randint(MIN_COUNT, MAX_COUNT) for _ in range(n)]
    max_count = 0
    max_number = []
    for i in set(array):
        a = array.count(i)
        if a > max_count:
            max_count = a
            max_number = [i]
        elif a == max_count:
            max_number.append(i)
    return max_count, max_number



def result_3(n):

    array = [random.randint(MIN_COUNT, MAX_COUNT) for _ in range(n)]
    counter = Counter(array)
    max_count = 0
    max_number = []
    for i in dict(counter):
        if dict(counter)[i] == max(counter.values()):
             max_number.append(i)
             max_count=max(counter.values())
    return max_number, max_count

print(timeit.timeit('result_1(500)', number=100, globals=globals()))   # 0.9497042139992118
print(timeit.timeit('result_1(1000)', number=100, globals=globals()))  # 2.8880962729999737
print(timeit.timeit('result_1(2500)', number=100, globals=globals()))  # 10.30093041699729
print(timeit.timeit('result_1(5000)', number=100, globals=globals()))  # 22.740271313999983
print(timeit.timeit('result_1(10000)', number=100, globals=globals())) # 47.95995621300244
print('*'*20)
print(timeit.timeit('result_2(500)', number=100, globals=globals()))   # 0.46066733600309817
print(timeit.timeit('result_2(1000)', number=100, globals=globals()))  # 1.4212180290051037
print(timeit.timeit('result_2(2500)', number=100, globals=globals()))  # 5.109205241999007
print(timeit.timeit('result_2(5000)', number=100, globals=globals()))  # 11.267301369000052
print(timeit.timeit('result_2(10000)', number=100, globals=globals())) # 23.080311656005506
print('*'*20)
print(timeit.timeit('result_3(500)', number=100, globals=globals()))   # 0.874567147999187
print(timeit.timeit('result_3(1000)', number=100, globals=globals()))  # 2.1049564750064746
print(timeit.timeit('result_3(2500)', number=100, globals=globals()))  # 4.591920735001622
print(timeit.timeit('result_3(5000)', number=100, globals=globals()))  # 5.467966074000287
print(timeit.timeit('result_3(10000)', number=100, globals=globals())) # 6.116221587995824



cProfile.run('result_1(10_000)')

#      50272 function calls in 0.457 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.003    0.003    0.020    0.020 1.py:11(<listcomp>)
#     1    0.437    0.437    0.456    0.456 1.py:9(result_1)
#     1    0.000    0.000    0.457    0.457 <string>:1(<module>)
# 10000    0.007    0.000    0.013    0.000 random.py:200(randrange)
# 10000    0.004    0.000    0.017    0.000 random.py:244(randint)
# 10000    0.005    0.000    0.007    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.457    0.457 {built-in method builtins.exec}
#     6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 10261    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

cProfile.run('result_2(10_000)')

#
#         51235 function calls in 0.241 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.241    0.241 1.py:28(result_2)
#         1    0.003    0.003    0.022    0.022 1.py:30(<listcomp>)
#         1    0.000    0.000    0.241    0.241 <string>:1(<module>)
#     10000    0.007    0.000    0.014    0.000 random.py:200(randrange)
#     10000    0.004    0.000    0.019    0.000 random.py:244(randint)
#     10000    0.005    0.000    0.007    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.241    0.241 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#      1000    0.218    0.000    0.218    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     10230    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('result_3(10_000)')
#       52272 function calls in 0.082 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.029    0.029    0.081    0.081 1.py:44(result_3)
#      1    0.004    0.004    0.026    0.026 1.py:46(<listcomp>)
#      1    0.000    0.000    0.082    0.082 <string>:1(<module>)
#      1    0.000    0.000    0.001    0.001 __init__.py:540(__init__)
#      1    0.000    0.000    0.001    0.001 __init__.py:608(update)
#      1    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
#  10000    0.009    0.000    0.017    0.000 random.py:200(randrange)
#  10000    0.005    0.000    0.022    0.000 random.py:244(randint)
#  10000    0.006    0.000    0.008    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
#      1    0.001    0.001    0.001    0.001 {built-in method _collections._count_elements}
#      1    0.000    0.000    0.082    0.082 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#   1002    0.025    0.000    0.025    0.000 {built-in method builtins.max}
#      2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#  10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  10255    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#   1002    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}




# 1 и 2 вариант имеют линейную зависимость, с увеличением значений в 10 раз, время увеличивается в 20 раз.
# 2 вариант меньше затрачивает времени в 2 раза, чем 1 вариант с  одинаковыми входными данными.
# 3 вариант использует коллекции, намного быстрее обрабатываюся данные , имеет кривую зависимость ,
# с  каждым увеличением данных  в 10 раз скорость выполнения в увеличивается в  2 раза.


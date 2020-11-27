import random
MIN_num=-100
MAX_NUM= 99

def babble(n):
    array = [random.randint(MIN_num, MAX_NUM) for _ in range(n)]
    print(f'Исходный массив- {array}')
    n = 0
    while n < len(array):
        count = 0
        for i in range((len(array) - 1) - n):

            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count += 1
        if count == 0:
            return array
        print(array)
        n += 1


print(f'Итоговый массив- {babble(10)}')

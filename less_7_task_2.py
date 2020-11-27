import random

SIZE = 10
MAX_NUM = 50
array = [random.uniform(0, MAX_NUM) for _ in range(SIZE)]


def merge_sort(data):
    count = len(data)
    if count > 2:
        part_1 = merge_sort(data[:count // 2])
        part_2 = merge_sort(data[count // 2:])
        data = part_1 + part_2
        last_index = len(data) - 1

        for a in range(last_index):
            min_value = data[a]
            min_index = a

            for b in range(a + 1, last_index + 1):
                if min_value > data[b]:
                    min_value = data[b]
                    min_index = b

            if min_index != a:
                data[a], data[min_index] = data[min_index], data[a]

    elif len(data) > 1 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]

    return data


print(merge_sort(array))

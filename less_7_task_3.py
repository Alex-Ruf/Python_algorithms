import random

MAX_NUM = 50
num = random.randint(0, 10)
data = [random.randrange(0, MAX_NUM) for _ in range(num * 2 + 1)]


def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return QuickSort(L) + M + QuickSort(R)


print(data)
print(f'Медиана массива {QuickSort(data)[num]}')

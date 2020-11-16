from collections import deque

a = deque(input("введите 1 число 16-ой системы ").upper())
b = deque(input("введите 2 число 16-ой системы ").upper())
c = deque()
p = deque()

list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

if len(a) < len(b):
    a, b = b, a

k=0
for i in range(1, len(a)+1):
    c.appendleft('0')
    k = (list_of_numbers.index(a[-i]) +k+ list_of_numbers.index(c[-i]))
    if i > len(b):
        c[-i]=(list_of_numbers[k % 16])

    else:
        k=(k + (list_of_numbers.index(b[-i])))
        c[-i]=(list_of_numbers[k % 16])
        if k>16:
            k=1
        else:
            k=0

if k==1:
    c.appendleft('1')


k = 0
for i in range(1, len(b) + 1):
    for q in range(1, len(a) + 1):
        if len(p) <= i + q - 1:
            p.appendleft("0")
        m = (list_of_numbers.index(a[-q]) * list_of_numbers.index(b[-i]) + k + list_of_numbers.index(p[-(i + q - 1)]))
        p[-(i + q - 1)] = (list_of_numbers[m % 16])
        if m > 15:
            k = m // 16
        else:
            k = 0
    if k != 0:
        if len(p) < i + q:
            p.appendleft(list_of_numbers[k])
        else:
            p[-len(p)] = (list_of_numbers[k])
        k = 0

print(f'Сумма - {list(c)}')
print(f'Произведение- {list(p)}')

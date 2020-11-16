from collections import namedtuple

a = []
n = int(input("Введите количество компаний: "))
Company = namedtuple('Company', 'name, one, two, three, four,total')
count = 0
while count != n:
    q = input("Название компании: ")
    w = int(input("Прибыль 1-й квартал: "))
    e = int(input("Прибыль 2-й квартал: "))
    r = int(input("Прибыль 3-й квартал: "))
    t = int(input("Прибыль 4-й квартал: "))
    sum_ = w + e + r + t
    company = Company(q, w, e, r, t, sum_)
    a.append(company)
    count += 1

total = 0
for i in range(n):
    total += a[i].total

print(f'{total / n}')
print(f'Выше среднего -', end=' ')
for i in range(n):
    if a[i].total > total / n:
        print(f'{a[i].name}', end=' ')
print()
print(f'Ниже среднего -', end=' ')
for i in range(n):
    if a[i].total < total / n:
        print(f' {a[i].name}', end=' ')

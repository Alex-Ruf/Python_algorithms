# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

count = 0
array = []

while count < 5:
    count += 1
    number = [int(num) for num in input(f'Введите {count} строку с 3-мя числами: ').split()]
    array.append(number)
for a in array:
    summa = 0
    for x, y in enumerate(a):
        summa += y
        print(f'{y:>5}', end="")
    print(f'{summa:>{len(str(summa)) + 4}}')

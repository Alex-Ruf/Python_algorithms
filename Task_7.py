# https://drive.google.com/file/d/1gRvpEIPaeyyR3nIIeM3MlD0tkRV8PcH2/view?usp=sharing

def sum_(i):
    if i == 1:
        return i
    summa = i + sum_(i - 1)
    return summa


i = int(input("Введите натуральное число n от 0 до 998: "))

a = sum_(i)
b = i * (i + 1) // 2

if a == b:
    p = 'Соответствует'
else:
    p = 'Не соответствует'
print(f'{a} {p} {b}')

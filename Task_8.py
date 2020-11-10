# https://drive.google.com/file/d/1gRvpEIPaeyyR3nIIeM3MlD0tkRV8PcH2/view?usp=sharing

CONST_NUM = 10

count_numbers = int(input("Введите количество чисел: "))
numeral = int(input("Введите любую цифру для поиска: "))
count = 0
for i in range(1, count_numbers + 1):
    num = int(input("Введите любое натуральное числo: "))
    while num > 0:
        if num % CONST_NUM == numeral:
            count += 1
        num = num // CONST_NUM

print(f'Колличество совпадений цифры {numeral} -  {count} раз(а)')

# https://drive.google.com/file/d/1gRvpEIPaeyyR3nIIeM3MlD0tkRV8PcH2/view?usp=sharing

from random import randint

number = randint(0, 100)
i = 0
shot = 10
print("Введите целое натуральное число от 0 до 100")
while i < shot:
    i += 1
    num = int(input(f"{i} -Попытка, введите число: "))
    if number == num:
        print(f'Угадали число!!! {number}')
        break;
    elif num < number:
        print(f'Загаданное число больше {num}')
    else:
        print(f'Загаданное число меньше {num}')
print(f'УПССС, не угадали число - было загадано: {number}')

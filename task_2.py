# https://drive.google.com/file/d/1gRvpEIPaeyyR3nIIeM3MlD0tkRV8PcH2/view?usp=sharing

number = int(input("Введите любое натуральное число: "))
even = 0
odd = 0
while number > 0:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    number = number // 10
print(f'Число четных цифр- {even}')
print(f'Число нечетных цифр- {odd}')

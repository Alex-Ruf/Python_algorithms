# https://drive.google.com/file/d/1gRvpEIPaeyyR3nIIeM3MlD0tkRV8PcH2/view?usp=sharing

num = input("Введите любое натуральное число: ")
even = 0
odd = 0
for i in map(int, num):
    if i % 2 == 0 or i == 0:
        even += 1
    else:
        odd += 1

print(f'Число четных цифр- {even}')
print(f'Число нечетных цифр- {odd}')

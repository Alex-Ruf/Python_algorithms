# https://drive.google.com/file/d/1gRvpEIPaeyyR3nIIeM3MlD0tkRV8PcH2/view?usp=sharing

MIN = 32
MAX = 127
COUNT = 10

for a in range(MIN, MAX + 1, COUNT):
    for i in range(a, a + COUNT):
        if i > MAX:
            break;
        else:
            print(f'\t{i} - {chr(i)}', end='')
    print()
